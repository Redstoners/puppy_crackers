from itertools import product
import msvcrt as m
import md5
import sys
import time

def wait():
	m.getch()

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}[]:;\|<>/?+=_-"
print("")
print("Input Hash")
hash = raw_input(">")
start = time.time()

for length in range(1, 21):
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		#print("".join(attempt))
		if hash == md5.md5("".join(attempt)).hexdigest():
			print("Found it!")
			print("")
			print("".join(attempt))
			end = time.time()
			print("")
			print(end - start)
			print("Seconds")
			print("")
			print("Press a button to continue")
			wait()
			sys.exit()
