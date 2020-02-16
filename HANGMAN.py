import random
from os import system,name
fname ="sowpods.txt" 
def clear(): 
	if name == 'nt': 
		_ = system('clear') 
def random_line(fname):
	lines = open(fname).read().splitlines()
	while len(random.choice(lines))<4:
		continue
	return random.choice(lines)
	
lives = 8
count = 0
word = random_line(fname)
guessed_letters = []
guess_word = []
print("Welcome to hangman!")
#initial print
for x in word:
	guess_word.append("_")
	print(guess_word[count]+" ", end = '')
	count+=1
while lives!=0 :
	clear()
	wrong = 0
	guess = input("\nPlease enter your guess letter :").upper()
	if guess == '':
		print("Your guess can't be empty")
		continue
	if guess == '_':
		print("Your guess has to be a letter")
		continue
	if guess in guessed_letters:
		print("You already guessed that")
		continue
	if guess.isdigit():
		print("Guess can't be a digit")
		continue
	if len(guess)>1:
		print("Guess can't be longer than one letter")
		continue
	count = 0
	for x in word :
		if x == guess:
			guess_word[count] = x
		else:
			wrong+=1
		print(guess_word[count]+" ", end = '')
		count+=1
	if wrong >= len(word):
		lives-=1
	print ("\nYou have %s wrong guesses left" % str(lives))
	guessed_letters.append(guess)
	if "$".join(guess_word) == "$".join(word):
		print("\nCongrats you won!")
		print("The word was : ", word)
		break
if "$".join(guess_word) != "$".join(word):
		print("\nToo bad you lost!")
		print("The word was : ", word)
			
