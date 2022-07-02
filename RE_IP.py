import re
str1 = 'Port-channel1.189     192.168.189.254  YES   CONFIG  up         up   '
show_interface = re.match('(\w+\-\w+\.\d+)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s',str1).groups()
# Get requested parameters from interface
print('-'*120)
print('{:<12}'.format('Interface') + '{:<3}'.format(':') + f'{show_interface[0]:<20}')
print('{:<12}'.format('IP Address') + '{:<3}'.format(':') + f'{show_interface[1]:<20}')
print('{:<12}'.format('Status') + '{:<3}'.format(':') + f'{show_interface[5]:<20}')
