#while循环的示例
number = 23
running = True

while running:
	guess = int(input('Enter an integer:'))

	if guess == number:   #键盘输入的数字直到跟给出的数字相同才退出循环
		print('Congratulations, you guessed it.')
		running = False
	elif guess < number:
		print('No, it is a little higher than that.')
	else:
		print('No, it is a little lower than that.')
else:
	print('The while loop is over.')

print('Done')