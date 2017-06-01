import random

cont = 'y' # For defining while loop exiting



def scorecard(number):   # who are getting a point
	if number == 1 :
		print('Draw')
		
	elif number == 2 :
		print('Computer got a point')
		
	
		
	elif number == 3:
		print('You got a point')
		


def choice(n):   # assing numbers for rock paper scissor of computer choice
	if n == 1 :
		print('Rock')
	elif n == 2 :
		print('Paper')
	elif n == 3 :
		print('scissors')



def user():
	user_input = input('choose anything \n1.rock \n2.paper \n3.scissors\n \n')
	game = (random.randint(1,3)) #computer choice of rock,paper scissor
	print('#'*50) # printint * 50 times for looking good in terminal
	choice(game)  # printing computer choice
	print('#'*50)
	'''these if else loop defines which beats which 
	for example paper beats rock '''
	if user_input == '1':
		if game == 1:
			scorecard(1)
		elif game == 2:
			scorecard(2)
		elif game == 3:
			scorecard(3)
	elif user_input == '2':
		if game == 1:
			scorecard(3)
		elif game == 2:
			scorecard(2)
		elif game == 3:
			scorecard(1)
	elif user_input == '3':
		if game == 1:
			scorecard(2)
		elif game ==2:
			scorecard(3)
		elif game ==3:
			scorecard(1)
	else:
		print('Enter a valid choice') # if user doesn't makes a valid choice



while cont == 'y' or cont == 'Y':
    
	r = user() # storing user value in r 
	print(r) # print r

	print('*'*50 +'\n'+'*'*50)
	cont = input (' Do you want to continue \'y\' for yes any key to exit :  ')
	print (cont)  # ask user weather he wants to continue or not
	print('*'* 50,'\n','*'*50 )


