#GUESS THE NUMBER
import random 

rand_number = random.randrange(0,20)
user_number = -1
	
	

while user_number != rand_number :
	user_number = input("Enter a number: ")
	if user_number.isdigit()  == False:
		print("please enter a valid number")
		continue
	user_number = int(user_number)
	if(user_number>rand_number):
		print("The random number is lower")
	if(user_number<rand_number):
		print("The random number is higher")
print("Congratulations, you guessed the number")

