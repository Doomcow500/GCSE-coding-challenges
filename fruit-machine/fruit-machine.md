The solution for Speed Tracker! 
```
import random

#possible rolls
symbols = ["Cherry","Bell","Lemon","Orange","Star","Skull"]
#startng money
money = 100

while money >= 20:
    print(f"your money is {money/100}")
    input("press enter to play, you need 0.2 money to do so! :)")

    #chooses the fruits
    possible = (symbols[random.randint(0,5)],symbols[random.randint(0,5)],symbols[random.randint(0,5)])

    # for 3 of the same
    if len(set(possible)) == 1:
        if "Bell" in possible:
            moneyChange = 500
        else:
            moneyChange = 100

    # for 2 of the same
    elif len(set(possible)) == 2:
        if possible.count("Skull") == 2:
            moneyChange = -100
        else:
            moneyChange = 50
    else:
         moneyChange = 0

    print(f"Rolled {possible}")
    #work out new money
    moneyChange -= 20
    money += moneyChange
    print (f"You won/lost {moneyChange/100} money")

print ("You're out of money, sorry.")
```
Yeilds an output of:
```
doomcow500@shush:~/projects$ python3 fruit-machine.py
your money is 1.0
press enter to play, you need 0.2 money to do so! :)
Rolled ('Cherry', 'Star', 'Skull')
You won/lost -0.2 money
your money is 0.8
```
