The solution to Theif! (requires itertools library)

Prerequisites:
itertools
''' pip install itertools'''

```
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
```
Output looks like:
```
doomcow500@shush:~/project$ python3 main.py 
What is your first number?1
What is your first number?2
What is your first number?3
What is your first number?4
{('1', '4', '2', '3'), ('4', '1', '2', '3'), ('3', '2', '4', '1'), ('1', '4', '3', '2'), ('3', '1', '4', '2'), ('4', '1', '3', '2'), ('3', '4', '2', '1'), ('1', '2', '3', '4'), ('4', '2', '3', '1'), ('3', '2', '1', '4'), ('1', '2', '4', '3'), ('4', '3', '1', '2'), ('2', '4', '1', '3'), ('2', '1', '3', '4'), ('4', '2', '1', '3'), ('2', '3', '4', '1'), ('1', '3', '2', '4'), ('3', '4', '1', '2'), ('2', '1', '4', '3'), ('1', '3', '4', '2'), ('3', '1', '2', '4'), ('4', '3', '2', '1'), ('2', '4', '3', '1'), ('2', '3', '1', '4')}
```
