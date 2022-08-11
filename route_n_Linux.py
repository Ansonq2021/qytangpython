# Grep gateway's IP in Linux
import re
import os

route_n_result = os.popen('route -n').read()
print (route_n_result)
for route in route_n_result.strip().split('\n')[2:]:
    re.route = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        r'(\w+)\s+\d+\s+\d+\s+\d+ \w+',
                        route.strip()).groups()
    print(re.route)
    if re.route[3] == 'UG':
        print('Gateway is : ' + re.route[1])
    break

# option B:
r = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s', route_n_result)
print(r)
print(route_n_result.split()[5] + ' is : ' + r[1])