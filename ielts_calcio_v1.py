import math
        
print('Please, input your assumed IELTS band scores:')

a = float(input("Input a band score for Speaking: "))

b = float(input("Input a band score for Listening: "))

c = float(input("Input a band score for Reading: "))

d = float(input("Input a band score for Writing: "))

o = (a + b + c + d)/4

print("Your Overall band score would be: ",math.ceil(o))



