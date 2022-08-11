import os
res = os.popen('ifconfig').read()
print(res)