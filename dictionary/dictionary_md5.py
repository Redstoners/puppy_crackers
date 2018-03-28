#PYTHONIOENCODING=utf-8
from itertools import product
import md5
import sys
import time

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
		if hash == md5.md5("".join(line)).hexdigest():
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
