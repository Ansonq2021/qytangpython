import re
MAC_Addr = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
show_mac_addr = re.match('(\d{1,4})\s+([\w]{4}\.[\w]{4}\.[\w]{4})\s+(\w+)\s+([\w/\/]{8})', MAC_Addr).groups()
print('{:<10}'.format('VLAN ID') + '{:<3}'.format(':') + f'{show_mac_addr[0]:<20}')
print('{:<10}'.format('MAC') + '{:<3}'.format(':') + f'{show_mac_addr[1]:<20}')
print ('{:<10}'.format('TYPE') + '{:<3}'.format(':') + f'{show_mac_addr[2]:<20}')
print('{:<10}'.format('Interface') + '{:<3}'.format(':') + f'{show_mac_addr[3]:<20}')