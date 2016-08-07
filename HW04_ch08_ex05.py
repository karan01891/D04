# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.




def rotate_word(word,number):
	updated_word =""
	for i in word:
		
		 #print (i)
		 convert = ord(i) + number % 26
		 #print (convert)
		 if 97 <= ord(i) <= 122 and convert > 122:
		 	convert = 97 + (convert - 122 - 1 ) 
		 	

		 elif 65 <= ord(i) <= 90 and convert > 90:
		 	convert = 65 + (convert - 90 - 1 ) 
		 updated_word += chr(convert)

	print(updated_word)
	
def main():
	word = input("Enter the word ")
	number = int(input("Enter the number "))
	rotate_word(word,number)

if __name__ == '__main__':	
	main()

