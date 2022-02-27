#!/usr/bin/python

number = 42
while True:
	print("Guess a number:")
	guess = input()
	guess = int(guess)
	if guess == number:
		print("Correct!")
		break
	else:
		print("Wrong!")
