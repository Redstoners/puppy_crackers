from itertools import product
import sys
import time
import pbkdf2


file = sys.argv[1]

hash = sys.argv[2]

salty = sys.argv[3]

try:
    start = time.time()
    with open(file) as f:
        line = f.readline()
        line = line.replace('\n','')
        line = line.replace('\t','')
        cnt = 1
        while line:
            line10 = "".join(line)
            hash_gen = pbkdf2.pbkdf2_hex(line10, salty, iterations=4096, keylen=256 / 8)
            #hash_objectsha1 = hashlib.sha1(line10)
            #hex_digsha1 = hash_objectsha1.hexdigest()
            if hash == hash_gen:
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
    sys.exit()
except:
    null = 0
