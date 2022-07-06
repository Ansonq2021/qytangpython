import re
ASA_Show_Conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
ASA_Conn_Para = re.split('[\s\,]', ASA_Show_Conn)
print(ASA_Show_Conn)
print('{:<12}'.format('Protocol') + '{:^3}'.format(':') + f'{ASA_Conn_Para[0]:<15}')
print(f'{ASA_Conn_Para[1]:<12}' + '{:^3}'.format(':') + f'{ASA_Conn_Para[2]:<15}')
print(f'{ASA_Conn_Para[3]:<12}' + '{:^3}'.format(':') + f'{ASA_Conn_Para[4]:<20}')
Time_Reformat = re.split('[:]', f'{ASA_Conn_Para[7]}')
Idle_Time = str(f'{Time_Reformat[0]}' + ' Hour ' + f'{Time_Reformat[1]}' + ' Minute ' f'{Time_Reformat[2]}' + ' Second ')
print(f'{ASA_Conn_Para[6]:<12}' + '{:^3}'.format(':') + f'{Idle_Time:<15}')
print(f'{ASA_Conn_Para[9]:<12}' + '{:^3}'.format(':') + f'{ASA_Conn_Para[10]:<15}')
print(f'{ASA_Conn_Para[12]:<12}' + '{:^3}'.format(':') + f'{ASA_Conn_Para[13]:<15}')



