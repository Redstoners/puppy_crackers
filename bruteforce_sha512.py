from itertools import product
import md5
import sys
import time
import hashlib

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}[]:;\|<>/?+=_-"
print("")
print("Input Hash")
hash = raw_input(">")
start = time.time()

for length in range(1, 4):
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		attempt10 = "".join(attempt)
		hash_objectsha512 = hashlib.sha512(attempt10)
		hex_digsha512 = hash_objectsha512.hexdigest()
		#print(attempt10)
		#print(hex_digsha512)
		if hash == hex_digsha512:
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
