import os
import re

route_n = 'Kernel IP routing table\
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface\
0.0.0.0         10.0.0.1        0.0.0.0         UG    100    0        0 ens33\
10.0.0.0        0.0.0.0         255.255.255.0   U     100    0        0 ens33'

r = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s', route_n)
print(r)
print(route_n.split())
print((route_n.split()[4] + ' is ' + re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s', route_n)[1]))

