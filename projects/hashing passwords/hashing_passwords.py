# -*- cofing: utf-8 -*-
import argparse
import hashlib

# parsing
parser = argparse.ArgumentParser(description='hashing given password')
parser.add_argument('password', help='input password you want to hash')
parser.add_argument('-t', '--type', default='sha256',choices=['sha256', 'sha512', 'md5'] )
args = parser.parse_args() 

# hashing given password
password = args.password
hashtype = args.type
m = getattr(hashlib,hashtype)()
m.update(password.encode())

# output
print("< hash-type : " + hashtype + " >")
print(m.hexdigest())
