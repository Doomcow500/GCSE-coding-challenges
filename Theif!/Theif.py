#imports itertools to make this much easier
import itertools

#asks for the four numbers and assigns them to variables
number1 = str(input("What is your first number?"))
number2 = str(input("What is your first number?"))
number3 = str(input("What is your first number?"))
number4 = str(input("What is your first number?"))

#makes an array with the variables
lst = [number1,number2,number3,number4]

#prints all of the possible permutations
print(set(itertools.permutations(lst)))
