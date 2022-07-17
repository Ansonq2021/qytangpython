import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
print(ifconfig_result)

ipv4_addr = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]

print(ipv4_addr)
