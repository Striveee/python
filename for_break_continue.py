#（1）for循环示例
#for i in range(0,5):
#	print(i)
#else:
#	print('the for loop is over')

#（2）break示例
#while True:
#	s = input('Enter something:')
#	if s=='quit':
#		break
#	print('Length if the string is', len(s))
#print('Done')

#（3）continue示例
while True:
	s = input('Enter something:')
	if s == 'quit':
		break
	if len(s) < 3:
		print('Too small')
		continue
	print('input is of sufficient length',len(s))
