# 13.05.23 | added try-except pair to check if the user input is a float number
# 12.05.23 | added a while loop to check if the score is between 0 and 9

import math

error_message = "Your score can only be an integer or an integer with a half!"

warning_message = "Please only input numbers between 1 and 9."

invalid_input_message = "Invalid input! Please enter a float number, such as 7.0 or 8.5."

# starting point of the program

print('\nPlease input your IELTS band scores:')

while True:
	user_input = input("\nInput a band score for Speaking: ")
	try:
		user_input = float(user_input)
		if isinstance(user_input, float):					# checking if the user input is a float number
			speaking_score = user_input
			if 0 <= speaking_score <= 9:					# checking if the number is between 0 and 9
				spk_diff = math.ceil(speaking_score)-speaking_score
				if spk_diff==0.5 or spk_diff==0:			# checking if the number ends with .0 or .5
					break
				else:	
					print(error_message)
			else:
				print(warning_message)
	except ValueError:
	    print(invalid_input_message)

while True:
	user_input = input("\nInput a band score for Listening: ")
	try:
		user_input = float(user_input)
		if isinstance(user_input, float):
			listening_score = user_input
			if 0 <= listening_score <= 9:
				lis_diff = math.ceil(listening_score)-listening_score
				if lis_diff==0.5 or lis_diff==0:
					break
				else:
					print(error_message)
			else:
				print(warning_message)
	except ValueError:
	    print(invalid_input_message)

while True:
	user_input = input("\nInput a band score for Reading: ")
	try:
		user_input = float(user_input)
		if isinstance(user_input, float):
			reading_score = user_input
			if 0 <= reading_score <= 9:
				read_diff = math.ceil(reading_score)-reading_score
				if read_diff==0.5 or read_diff==0:
					break
				else:
					print(error_message)
			else:
				print(warning_message)
	except ValueError:
	    print(invalid_input_message)				

while True:
	user_input = input("\nInput a band score for Writing: ")
	try:
		user_input = float(user_input)
		if isinstance(user_input, float):
			writing_score = user_input
			if 0 <= writing_score <= 9:
				wrt_diff = math.ceil(writing_score)-writing_score
				if wrt_diff==0.5 or wrt_diff==0:
					break
				else:
					print(error_message)
			else:
				print(warning_message)
	except ValueError:
	    print(invalid_input_message)

def ielts_calc(a,b,c,d):

	ovr = (a + b + c + d)/4

	q = (ovr*100 % 100)*10

	reply = "\nYour overall band score is: "

	if q >= 750:
		print(reply, math.ceil(ovr))

	elif q <= 125:
		print(reply, math.floor(ovr))

	elif 250 <= q <= 650:
		print(reply, math.floor(ovr) + 0.5)

a = speaking_score

b = listening_score

c = reading_score

d = writing_score

ielts_calc(a,b,c,d)