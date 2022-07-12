import os
import re

ens160 = 'flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255\
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>\
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)\
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)\
              RX errors 1 dropped 24662 overruns 0 frame 0\
              TX packets 51706604 bytes 41788673420 (38.9 GiB)\
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0'
ifconfig_result = os.popen('ifconfig' + 'ens160').read()
# Lookup IP, mask, broadcast IP and MAC:
ipv4_addr = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ens160)[0]
netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ens160)[0]
broadcast = re.findall(r'broadcast \d{1,3}\.\d{1,3}\.\d{1,3}\.{1,3}', ens160)[0]
mac_addr = re.findall(r'ether ([\w]{2}:[\w]{2}:[\w]{2}:[\w]{2}:[\w]{2}:[\w]{2})', ens160)[0]
print('{:<12}'.format('ipv4_addr') + '{:}'.format(':') + '{}'.format(ipv4_addr))
print('{:<12}'.format('netmask') + '{:}'.format(':') + '{}'.format(netmask))
print('{:<12}'.format('broadcast') + '{:}'.format(':') + '{}'.format(netmask))
print('{:<12}'.format('mac_addr') + '{:}'.format(':') + '{}'.format(mac_addr))
ipv4_list_1 = re.split('[.]', ipv4_addr)
ipv4_list_1[3] = '254'
ipv4_gw = '.'.join(ipv4_list_1)
print(ipv4_gw)
print('\nAssuming last octet of Gateway IP address is 254, then Gateway IP is: '+ ipv4_gw + '\n')
#ping_result = os.popen('ping ') + ipv4_gw + ' -c 1').read()
#if re_ping_result:
#    print('Gateway reachable!')
#else:
#    print('Gateway unreachable!')
