import random
comp = 0
you = 0
def scorecard(number):
	if number == 1 :
		print('Draw')
		
	elif number == 2 :
		print('Computer got a point')
		comp = comp + 1
		
	elif number == 3:
		print('You got a point')
		you = you + 1
	print('comp **** you')
	print(comp+ '    ' + you)
		

def choice(n):
	if n == 1 :
		print('Rock')
	elif n == 2 :
		print('Paper')
	elif n == 3 :
		print('scissors')



def user():
	user_input = input('choose anything \n1.rock \n2.paper \n3.scissors\n \n')
	game = (random.randint(1,3))
	print('#'*50)
	choice(game)
	print('#'*50)
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
		print('Enter a valid choice')

while 1 == 1:

	user()
	print('*'*50 +'\n'+'*'*50)



