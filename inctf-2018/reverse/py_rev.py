print "enter your input"
your_input=raw_input()
secret=''
key=(((125>>3)+5)/4)+15
for i in your_input:
	secret+=chr(ord(i)^key)
secret=secret.encode('hex')
if(secret=='7d7a7760726f4720667020664b567c202220604b47257a227c4b6320674b7c25674b7a20797169'):
	print ("Yes, you are right...\nMay the sun in his course visit..\nno land more free, more happy,\nmore lovely,\nthan this our country!")
else:
	print "Try again...\nIndians cannot forget him that easily"
