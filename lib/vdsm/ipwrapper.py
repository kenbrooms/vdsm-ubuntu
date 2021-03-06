# Copyright 2013 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

from netaddr.core import AddrFormatError
from netaddr import IPAddress
from netaddr import IPNetwork

from utils import CommandPath
from utils import execCmd

_IP_BINARY = CommandPath('ip', '/sbin/ip')


def _isValid(ip, verifier):
    try:
        verifier(ip)
    except (AddrFormatError, ValueError):
        return False

    return True


class Route(object):
    def __init__(self, network, ipaddr=None, device=None, table=None):
        if not _isValid(network, IPNetwork):
            raise ValueError('network %s is not properly defined' % network)

        if ipaddr and not _isValid(ipaddr, IPAddress):
            raise ValueError('ipaddr %s is not properly defined' % ipaddr)

        self.network = network
        self.ipaddr = ipaddr
        self.device = device
        self.table = table

    @classmethod
    def parse(cls, text):
        """
        Returns a dictionary populated with the route attributes found in the
        textual representation.
        """
        route = text.split()
        """
        The network / first column is required, followed by key+value pairs.
        Thus, the length of a route must be odd.
        """
        if len(route) % 2 == 0:
            raise ValueError('Route %s: The length of the textual '
                             'representation of a route must be odd.' % text)

        network, params = route[0], route[1:]
        data = dict(params[i:i + 2] for i in range(0, len(params), 2))
        data['network'] = '0.0.0.0/0' if network == 'default' else network
        return data

    @classmethod
    def fromText(cls, text):
        """
            Creates a Route object from a textual representation. For the vdsm
            use case we require the network IP address and interface to reach
            the network to be provided in the text.

            Examples:
            'default via 192.168.99.254 dev eth0':
            '0.0.0.0/0 via 192.168.99.254 dev eth0 table foo':
            '200.100.50.0/16 via 11.11.11.11 dev eth2 table foo':
        """
        data = cls.parse(text)
        try:
            ipaddr = data['via']
        except KeyError:
            raise ValueError('Route %s: Routes require an IP address.' % text)
        try:
            device = data['dev']
        except KeyError:
            raise ValueError('Route %s: Routes require a device.' % text)
        table = data.get('table')

        return cls(data['network'], ipaddr=ipaddr, device=device, table=table)

    def __str__(self):
        str = '%s via %s dev %s' % (self.network, self.ipaddr, self.device)

        if self.table:
            str += ' table %s' % self.table

        return str

    def __iter__(self):
        for word in str(self).split():
            yield word


class Rule(object):
    def __init__(self, table, source=None, destination=None, srcDevice=None):
        if source:
            if not (_isValid(source, IPAddress) or
                    _isValid(source, IPNetwork)):
                raise ValueError('Source %s invalid: Not an ip address '
                                 'or network.' % source)

        if destination:
            if not (_isValid(destination, IPAddress) or
                    _isValid(destination, IPNetwork)):
                raise ValueError('Destination %s invalid: Not an ip address '
                                 'or network.' % destination)

        self.table = table
        self.source = source
        self.destination = destination
        self.srcDevice = srcDevice

    @classmethod
    def parse(cls, text):
        rule = text.split()
        parameters = rule[1:]

        if len(rule) % 2 == 0:
            raise ValueError('Rule %s: The length of a textual representation '
                             'of a rule must be odd. ' % text)

        return dict(parameters[i:i + 2] for i in range(0, len(parameters), 2))

    @classmethod
    def fromText(cls, text):
        """
            Creates a Rule object from a textual representation. Since it is
            used for source routing, the source network specified in "from" and
            the table "lookup" that shall be used for the routing must be
            specified.

            Examples:
            32766:    from all lookup main
            32767:    from 10.0.0.0/8 to 20.0.0.0/8 lookup table_100
            32768:    from all to 8.8.8.8 lookup table_200
        """
        data = cls.parse(text)
        try:
            table = data['lookup']
        except KeyError:
            raise ValueError('Rule %s: Rules require "lookup" information. ' %
                             text)
        try:
            source = data['from']
        except KeyError:
            raise ValueError('Rule %s: Rules require "from" information. ' %
                             text)

        destination = data.get('to')
        if source == 'all':
            source = None
        if destination == 'all':
            destination = None
        srcDevice = data.get('dev') or data.get('iif')

        return cls(table, source=source, destination=destination,
                   srcDevice=srcDevice)

    def __str__(self):
        str = 'from '
        if self.source:
            str += self.source
        else:
            str += 'all'
        if self.destination:
            str += ' to %s' % self.destination
        if self.srcDevice:
            str += ' dev %s' % self.srcDevice

        str += ' table %s' % self.table

        return str

    def __iter__(self):
        for word in str(self).split():
            yield word


class IPRoute2Error(Exception):
    pass


def _execCmd(command):
    returnCode, output, error = execCmd(command)

    if returnCode:
        raise IPRoute2Error(error)

    return output


def routeList():
    command = [_IP_BINARY.cmd, 'route']
    return _execCmd(command)


def routeShowAllDefaultGateways():
    command = [_IP_BINARY.cmd, 'route', 'show', 'to', '0.0.0.0/0', 'table',
               'all']
    return _execCmd(command)


def routeShowTable(table):
    command = [_IP_BINARY.cmd, 'route', 'show', 'table', table]
    return _execCmd(command)


def routeAdd(route):
    command = [_IP_BINARY.cmd, 'route', 'add']
    command += route
    _execCmd(command)


def routeDel(route):
    command = [_IP_BINARY.cmd, 'route', 'del']
    command += route
    _execCmd(command)


def ruleList():
    command = [_IP_BINARY.cmd, 'rule']
    return _execCmd(command)


def ruleAdd(rule):
    command = [_IP_BINARY.cmd, 'rule', 'add']
    command += rule
    _execCmd(command)


def ruleDel(rule):
    command = [_IP_BINARY.cmd, 'rule', 'del']
    command += rule
    _execCmd(command)
