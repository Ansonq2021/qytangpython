department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_PYTHON = 1234.3456

line1 = 'Department1 name:%-11s Manager:%-11s COURSE FEES:%-12.5f %11s' % ('Security', 'cq_bomb', 456789.12456, 'The END!')
line2 = 'Department2 name:%-11s Manager:%-11s COURSE FEES:%-9.4f %14s' % ('Python', 'qinke', 1234.3456, 'The END!')


length = len(line1)
print ('='*length)
print (line1)
print (line2)
print ('='*length)