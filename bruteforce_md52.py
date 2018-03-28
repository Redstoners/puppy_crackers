from itertools import product
import sys
import time
import hashlib

def encrypt(str):
	hash_objectmd5 = hashlib.md5(str)
	#hash_objectmd5 = hashlib.md5(attempt10.encode())
	output = hash_objectmd5.hexdigest()
	return output

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}[]:;\|<>/?+=_-"
print("")
print("Input Hash")
#hash = input(">")
hash = raw_input(">")
start = time.time()

for length in range(1, 21):
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		attempt10 = "".join(attempt)
		output = encrypt(attempt10)
		print(attempt10)
		#print(hex_digmd5)
		if hash == output:
			print("Found it!")
			print("")
			print("".join(attempt))
			end = time.time()
			print("")
			print(end - start)
			print("Seconds")
			print("")
			raw_input("Press Enter to terminate.")
			#input("Press Enter to terminate.")
			sys.exit()
