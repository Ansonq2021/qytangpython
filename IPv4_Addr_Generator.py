import random

# Generate randomly IPv4 address
Random_IPv4_Addr = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
    random.randint(0, 255)) + '.' + str(random.randint(0, 255))
print(Random_IPv4_Addr)


