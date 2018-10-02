# This is a simple calcultor that gives the result as per the desired operation asked by the user.
# It does not use 'math library'.
# It extract the string input without invoking any error. 

import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")
previous = 0
run = True

def perform():
    global run
    global previous 
    
    equation = ""
    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(previous))
    
    if equation == 'quit':
        print("Goodbye, person.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("Result = ", previous)
while run:
    perform()