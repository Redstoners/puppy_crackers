from itertools import product
import sys
import time
import hashlib

print("Input dictionary")
file = raw_input(">")
print("Input Hash")
hash = raw_input(">")
start = time.time()

with open(file) as f:
	line = f.readline()
	line = line.replace('\n','')
	line = line.replace('\t','')
	cnt = 1
	while line:
		line10 = "".join(line)
		hash_objectsha384 = hashlib.sha384(line10)
		hex_digsha384 = hash_objectsha384.hexdigest()
		if hash == hex_digsha384:
			print("Found it!")
			print("")
			print("".join(line))
			end = time.time()
			print("")
			print(end - start)
			print("Seconds")
			print("")
			raw_input("Press Enter to terminate")
			sys.exit()
		line = f.readline()
		line = line.replace('\n','')
		line = line.replace('\t','')
		cnt += 1
print("Not succesful")
