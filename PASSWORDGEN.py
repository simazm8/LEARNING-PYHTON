import sys
import random

letters_all = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pass_length = input("How many characters do you want your password to be? ")
password = ""
if pass_length.isdigit():
	pass_length = int(pass_length)
	letters = input("How many letters do you want your password to contain? ")
	if letters.isdigit():
		letters = int(letters)
		numbers = pass_length-letters
		count = 0
		lettercount = 0
		numbercount = 0
		while (count<pass_length):
			char = random.randrange(2)
			#char == 0 then type random letter
			#char == 1 then type random number
			if((char == 0 and lettercount<letters) or numbercount == numbers):
				#upper == 0 type lower case
				#upper == 1 type upper case
				upper = random.randrange(2)
				if(upper == 0):
					password+=random.choice(letters_all)
				elif(upper == 1):
					password+=random.choice(letters_all).upper()
				lettercount+=1
			elif((char == 1 and numbercount<numbers) or lettercount == letters):
				password+=str(random.randrange(10))
				numbercount+=1
			count+=1
			print("numbercount: ",numbercount)
			print("lettercount: ",lettercount)
			print("password : " , password)
			print("\n")
		print(password)
	else:
		sys.exit("The number of letters can't exceed length of password")
else:
	sys.exit("Length has to be a number")
#6 CHAR
#letters = 1 
#password 
#numbercount = 1
#lettercount = 1
#count = 2