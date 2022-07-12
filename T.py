import re

ens160 = 'flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500\
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255\
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>\
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)\
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)\
              RX errors 1 dropped 24662 overruns 0 frame 0\
              TX packets 51706604 bytes 41788673420 (38.9 GiB)\
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0'
ipv4_addr = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ens160)[0]
ipv4_addr_list = (re.split('[.]', ipv4_addr)) + ipv4_addipv4_addr = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ens160)[0]r_list[4]

ipv4_addr_list = (re.split('[.]', ipv4_addr)) + ipv4_addipv4_addr = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ens160)[0]r_list[4]
print(f'{ipv4_addr_list[0]}{ipv4_addr_list[1]}{ipv4_addr_list[]2}ipv4_addr_list)

# print(gw)
