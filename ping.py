import os
hostname = "8.8.8.8"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(hostname, "is up!")
else:
    print(hostname, "is down!")
