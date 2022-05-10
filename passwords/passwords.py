import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]

def crackPassword1(user, hashedPW):
	hashes = 0
	for word in words:
		encoded_word = word.encode('utf-8')
		hasher = hashlib.sha256(encoded_word)
		digest = hasher.digest()
		digest_as_hex = binascii.hexlify(digest)
		hashes += 1
		if str(digest_as_hex)[2:-1] == hashedPW:
			print(user + ":" + word)
			return hashes

def crackPassword2(user, hashedPW):
	for word1 in words:
		for word2 in words:
			pair = word1 + word2
			print(pair)
			encoded_pair = pair.encode('utf-8')
			hasher = hashlib.sha256(encoded_pair)
			digest = hasher.digest()
			digest_as_hex = binascii.hexlify(digest)
			if str(digest_as_hex)[2:-1] == hashedPW:
				return (user, pair)

def crackPassword3(user, salt, hashedPW):
	for word in words:
		pw = salt + word
		encoded_pw = pw.encode('utf-8')
		hasher = hashlib.sha256(encoded_pw)
		digest = hasher.digest()
		digest_as_hex = binascii.hexlify(digest)
		if str(digest_as_hex)[2:-1] == hashedPW:
			return (user, word)

def part1():
	hashes = 0
	cracked = 0
	for line in open('pw1.txt'):
		firstColon = line.find(':')
		secondColon = line[firstColon+1:].find(':') + firstColon + 1
		user = line[:firstColon]
		hashedPW = line[firstColon+1:secondColon]
		hashes += crackPassword1(user, hashedPW)
		cracked += 1
	print("Hashes: " + str(hashes))
	print("Cracked: " + str(cracked))

def part2():
	for line in open('pw2.txt'):
		firstColon = line.find(':')
		secondColon = line[firstColon+1:].find(':') + firstColon + 1
		user = line[:firstColon]
		hashedPW = line[firstColon+1:secondColon]
		print(crackPassword2(user, hashedPW))

def part3():
	for line in open('pw3.txt'):
		line = "jondich:e75fa822$8a604057b98aff07885d29eea97e885e::0:99999:7:::"
		firstColon = line.find(':')
		dollarSign = line.find('$')
		secondColon = line[firstColon+1:].find(':') + firstColon + 1
		user = line[:firstColon]
		salt = line[firstColon+1:dollarSign]
		hashedPW = line[dollarSign+1:secondColon]
		print(crackPassword3(user, salt, hashedPW))

if __name__ == '__main__':
	part1()