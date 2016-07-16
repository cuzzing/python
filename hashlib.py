import hashlib

#sha1 = hashlib.sha1()
#sha1.update('how to use sha1 in '.encode('utf-8'))
#sha1.update('python hashlib?'.encode('utf-8'))
#print(sha1.hexdigest())

def calc_sha1(s):
	sha1 = hashlib.sha1()
	sha1.update(s.encode('utf-8'))
	return print(sha1.hexdigest())

s = input()
while not s == 'exit':
	calc_sha1(s)
	s = input()
