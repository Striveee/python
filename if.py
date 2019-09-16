#在python中有三种控制流语句——if、for和while

#if语句示例
#注：if、elif、else的主体都需要进行缩进，所处的行末都应该加“：”，否则出错
number  = 23   #定义的数字
guess = int(input('Enter an integer:'))    #从键盘获取的数字

if guess == number:
	print('Congratulations, you guessed it.')
	print('(But you do not win any prizes!)')

elif guess < number:
	print('No, it is a little higher than that')

else:
	print('No, it is a little lower than that')

print('Done')    #最后一句在if语句执行完成后执行
