#!/usr/bin/env python3

randnum = 50

if randnum < 0:
	message = 'is negative'
	print(randnum, message)
elif randnum > 0:
	message = 'is positive'
	print(randnum, message)
	if randnum < 50:
		message = 'is less than 50'
		print(randnum, message)	
	if randnum%2 is 0:
		message = 'is even'
		print(randnum, message)
	if randnum<50 and randnum%2 is 0:
		message = 'it is an even number that is smaller than 50'
		print(randnum, message)
	if randnum > 50:
		message = 'is greater than 50'
		print(randnum, message)
	if randnum % 3 is 0:
		message = 'is divisible by 3'
		print(randnum, message)
	if randnum > 50 and randnum % 3 is 0:
		message = 'is greater than 50 and divisible by 3'
		print(randnum,message)
else:
	message = 'is zero'
	print(randnum, message)
