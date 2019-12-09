#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib , os , string
from string import *

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

string_list = ascii_letters

def generateHashFromString(hashMethod, cleartextString):
    if hashMethod == "md5":
        return hashlib.md5(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha1":
        return hashlib.sha1(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha224":
        return hashlib.sha224(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha256":
        return hashlib.sha256(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha384":
        return hashlib.sha384(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha512":
        return hashlib.sha512(cleartextString.encode()).hexdigest()
    else:
        pass

def reverseString(string):
    return string[::-1]

def IndexErrorCheck(index_input):
    if len(string_list) <= index_input:
        pass
    else:
        return string_list[index_input]

def StringGenerator(string):
    if len(string) <= 0:
        string.append(string_list[0])
    else:
        # error checking needs to be done, otherwise a ValueError will raise
        string[0] = IndexErrorCheck((string_list.index(string[0]) + 1) % len(string_list))
        if string_list.index(string[0]) == 0:
            return [string[0]] + StringGenerator(string[1:])
    return string

def demd5():
    hashMethod = "md5"
    stringToBeCracked = str(input(' Input Hash : '))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(" String : {}".format(formatted_string))
            print ('')
            exit()

def desha1():
    hashMethod = "sha1"
    stringToBeCracked = str(input(' Input Hash : '))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(" String : {}".format(formatted_string))
            print ('')
            exit()

def desha224():
    hashMethod = "sha224"
    stringToBeCracked = str(input(' Input Hash : '))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(" String : {}".format(formatted_string))
            print ('')
            exit()

def desha256():
    hashMethod = "sha256"
    stringToBeCracked = str(input(' Input Hash : '))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(" String : {}".format(formatted_string))
            print ('')
            exit()

def desha384():
    hashMethod = "sha384"
    stringToBeCracked = str(input(' Input Hash : '))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(" String : {}".format(formatted_string))
            print ('')
            exit()

def desha512():
    hashMethod = "sha512"
    stringToBeCracked = str(input(' Input Hash : '))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(" String : {}".format(formatted_string))
            print ('')
            exit()

def menu() :
	print ('')
	print (' 01) : Decode MD5')
	print (' 02) : Decode SHA1')
	print (' 03) : Decode SHA224')
	print (' 04) : Decode SHA256')
	print (' 05) : Decode SHA384')
	print (' 06) : Decode SHA512')
	print ('')

def main() :
	cmd = str(input(' Menu : '))
	if cmd == '1' :
		demd5()
	elif cmd == '2' :
		desha1()
	elif cmd == '3' :
		desha224()
	elif cmd == '4' :
		desha256()
	elif cmd == '5' :
		desha384()
	elif cmd == '6' :
		desha512()

menu()
main()