department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_PYTHON = 1234.3456

line1 = 'Department1 name:%-16s Manager:%-16s COURSE FEES:%-12.5f %16s' % ('Security', 'cq_bomb', 456789.12456, 'The END!')
line2 = 'Department2 name:%-16s Manager:%-16s COURSE FEES:%-9.4f %19s' % ('Python', 'qinke', 1234.3456, 'The END!')

line1 = f'Department1: {department1:<16} Manager: {depart1_m:<16} COURSE FEES: {COURSE_FEES_SEC:12.5f}' + '{:>16}'.format('The END!')
line2 = f'Department2: {department2:<16} Manager: {depart2_m:<16} COURSE FEES: {COURSE_FEES_PYTHON:9.4f}' + '{:>19}'.format('The END!')

length = len(line1)
print ('='*length)
print (line1)
print (line2)
print ('='*length)