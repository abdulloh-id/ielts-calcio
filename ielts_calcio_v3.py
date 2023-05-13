# Calculating overall IELTS band score using a function

import math

print('\nPlease, input your assumed IELTS band scores:')

lis = float(input("\nInput a band score for Listening: "))

rea = float(input("\nInput a band score for Reading: "))

wrt = float(input("\nInput a band score for Writing: "))

spk = float(input("\nInput a band score for Speaking: "))

def ielts_calc(a,b,c,d):

	ovr = (lis + rea + wrt + spk)/4

	q = (ovr*100 % 100)*10

	if 0 < lis <= 9 and 0 < rea <= 9 and 0 < wrt <= 9 and 0 < spk <= 9:

		reply = "\nYour Overall band score would be: "

		if 0<math.ceil(lis)-lis<0.5 or 0<math.ceil(rea)-rea<0.5 or 0<math.ceil(wrt)-wrt<0.5 or 0<math.ceil(spk)-spk<0.5:
			print("\nYour scores only can be integers or integers with a half!")

		elif math.ceil(lis)-lis>0.5 or math.ceil(rea)-rea>0.5 or math.ceil(wrt)-wrt>0.5 or math.ceil(spk)-spk>0.5:
			print("\nYour scores only can be integers or integers with a half!")

		else:
			if q >= 750:
				print(reply, math.ceil(ovr))

			elif q <= 125:
				print(reply, math.floor(ovr))

			elif 250 <= q <= 650:
				print(reply, math.floor(ovr) + 0.5)
	else:
		print("\nPlease, input numbers between 1 and 9.")

z = ielts_calc

z(lis,rea,wrt,spk)