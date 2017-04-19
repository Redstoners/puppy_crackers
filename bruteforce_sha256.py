from itertools import product
import msvcrt as m
import md5
import sys
import time
import hashlib

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
		attempt10 = "".join(attempt)
		hash_objectsha256 = hashlib.sha256(attempt10)
		hex_digsha256 = hash_objectsha256.hexdigest()
		#print(attempt10)
		#print(hex_digsha256)
		if hash == hex_digsha256:
			print("Found it!")
			print("")
			print("".join(attempt))
			end = time.time()
			print("")
			print(end - start)
			print("Seconds")
			print("")
			print("Press a button to continue")
			raw_input("Press Enter to terminate.")
			sys.exit()
