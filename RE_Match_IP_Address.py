import re
str1 = 'Port-channel1.189     192.168.189.254    YES   CONFIG   up'
re.match('[A-Za-z]+\d\.\d+\s+\d{1,3}\.*', str1)
str1
