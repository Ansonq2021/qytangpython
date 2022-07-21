import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
print(ifconfig_result)
# Lookup IP, mask, broadcast IP and MAC:
ipv4_addr = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall(r'broadcast \d{1,3}\.\d{1,3}\.\d{1,3}\.{1,3}', ifconfig_result)[0]
mac_addr = re.findall(r'ether (\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})', ifconfig_result)[0]

print('{:<12}'.format('ipv4_addr') + '{:}'.format(':') + '{}'.format(ipv4_addr))
print('{:<12}'.format('netmask') + '{:}'.format(':') + '{}'.format(netmask))
print('{:<12}'.format('broadcast') + '{:}'.format(':') + '{}'.format(netmask))
print('{:<12}'.format('mac_addr') + '{:}'.format(':') + '{}'.format(mac_addr))

ipv4_list_1 = re.split('[.]', ipv4_addr)
ipv4_list_1[3] = '1'
ipv4_gw = '.'.join(ipv4_list_1)
print('\nAssuming last octet of Gateway IP address is 1, then Gateway IP is: ' + ipv4_gw + '\n')

ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result = re.findall(r'1 received', ping_result)
if re_ping_result:
    print('Gateway reachable!')
else:
    print('Gateway unreachable!')
