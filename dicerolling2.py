import random
import time as t

def action(choice):
    sum_h=sum_b=0
    print("Okay! Go for it!")
    t.sleep(1)
    for die in range(0, choice):
        human=random.randint(1, 6)
        t.sleep(1)
        print("You got:",human)
        sum_h+=human
    t.sleep(1)
    print("\nYOUR TOTAL IS:",sum_h)
    t.sleep(1)
    print("\nNow it's my turn")
    t.sleep(1)

    for die in range(0,choice):
        bot=random.randint(1,6)
        t.sleep(1)
        print("You got:", bot)
        sum_b+=bot
    t.sleep(1)
    print("\nYOUR TOTAL IS:",sum_b)
    t.sleep(2)

    result = "\nYOU WIN" if sum_h>sum_b else "\nI WIN" if sum_h<sum_b else "IT'S A TIE."
    
    print(result)
    if sum_h<sum_b:
        print("Thank God")
    elif sum_h<sum_b:
        print("Put in the work")
    t.sleep(1)      

def play():
    die=0
    roll =" "
    while die==0:
        choice = int(input("How many dice do you want to throw?(1-3)"))
        if choice>0 and choice <4:
            action(choice)
            break
        else:
            print("Please enter a valid choice.")

    print("Do you want to continue?(yes/no)")
    while roll!="yes":
        roll=input().lower().capitalize()
        if roll=="yes":
            play()
        else:
            print("It was nice playing with you!bye!")
            break    
play()               