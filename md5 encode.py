import md5

print('input string')
text = raw_input('>')
print md5.md5("".join(text.decode('utf-8'))).hexdigest()
