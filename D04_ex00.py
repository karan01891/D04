#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#	  - creates a random integer from 1 - 25
#	  - asks the user to guess what the number is
#	  - validates input is a number
#	  - tells the user if they guess correctly
#		  - if not: tells them too high/low
#	  - only lets the user guess five times
#		  - then ends the program
################################################################################
# Imports
import random
num = random.randint (1,25)
#print (num)

# Body

def guess():
	count = 0
	while count < 5:
		user_guess = int(input ("Enter your guess") )
		if (num > user_guess):
			print ("Your guess is too low")
			count += 1
			#print (count)
			continue
		elif (num < user_guess):
			print ("Your guess is too high")
			count += 1
			#print(count)
			continue
	 
		else:
			print("Bingo")
			break

	print ("Out of guesses")
################################################################################
def main():


	guess() # Remove this and replace with your function calls
	

if __name__ == '__main__':
	main()