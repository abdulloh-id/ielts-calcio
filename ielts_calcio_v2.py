import math
        
print('Please, input your assumed IELTS band scores:')

a = float(input("Input a band score for Listening: "))

b = float(input("Input a band score for Reading: "))

c = float(input("Input a band score for Writing: "))

d = float(input("Input a band score for Speaking: "))

o = (a + b + c + d)/4

q = (o*100 % 100)*10

if q >= 750:
    print("Your Overall band score would be: ",math.ceil(o))

elif q <= 125:
    print("Your Overall band score would be: ",math.floor(o))

elif q >= 250 or q <= 625:
    print("Your Overall band score would be: ",math.floor(o) + 0.5)
