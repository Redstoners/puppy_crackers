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

for length in range(1, 21):
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		attempt10 = "".join(attempt)
		hash_objectsha384 = hashlib.sha384(attempt10)
		hex_digsha384 = hash_objectsha384.hexdigest()
		#print(attempt10)
		#print(hex_digsha384)
		if hash == hex_digsha384:
			print("Found it!")
			print("")
			print("".join(attempt))
			end = time.time()
			print("")
			print(end - start)
			print("Seconds")
			print("")
			raw_input("Press Enter to terminate.")
			sys.exit()
