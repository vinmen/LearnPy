import os

with open(os.path.dirname(os.path.realpath(__file__)) + "/user_log.txt") as f:
	data = f.read().splitlines()
	
users = []
hs = open("users.txt", "a")
	
for line in data:
	if line.find("PW:") > -1:
		username = line[line.find("USER:") + 5:line.find("|PW:")]
	elif line.find("|IP:") > -1:   
		username = line[line.find("USER:") + 5:line.find("|IP:")]	
	
	if username.lower() not in users:
		users.append(username.lower())		
		hs.write(username.lower() + "\n")

hs.close() 
