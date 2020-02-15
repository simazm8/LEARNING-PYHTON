#ROCK PAPER SCISSORS
import random

possible_answers = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
input_string = "Please choose between rock, paper or scissors: "

print("Write 'stop' to stop the game")
user_answer = ""

while True:
	user_answer = input(input_string).lower()
	if user_answer == 'stop':
		break
	if user_answer not in possible_answers:
		print("Please enter a valid choice")
		continue
	computers_answer = possible_answers[random.randrange(0,3)]
	print("You chose: ", user_answer)
	print("The computer chose: ", computers_answer)
	if user_answer == computers_answer:
		print("It's a draw")
	if (computers_answer == "rock" and user_answer == "paper" or
	computers_answer == "paper" and user_answer == "scissors" or 
	computers_answer == "scissors" and user_answer == "rock") :
		print("You won this round")
		user_score+=1
	else:
		print("The computer won this round")
		computer_score+=1
	print("\n")
	print("The score:\n user: %d \n computer: %d" % (user_score,computer_score))

print("The final score:\n user: %d \n computer: %d" % (user_score,computer_score))
