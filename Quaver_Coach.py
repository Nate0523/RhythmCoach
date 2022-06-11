from time import sleep
from random import random
import math
from colorama import Fore, Back, Style
from colorama import init as coloramaInit
coloramaInit()
from os import name, system

def clear():
    if name=="nt":
        system("cls")
    else:
        system("clear")

error = ""
loop = True
while loop:
    while True:
        clear()
        print(error+"\n")
        error = ""
        evaltime = input("Game evaluation time (Time to think about how you did): ")
        breaktime = input("Break length (Recommended time is 80): ")
        minimum = input("Minimum amount of push-ups: ")
        maximum = input("Maximum amount of push-ups: ")
        freq = input("Push-up frequency (putting in 0.5 would be a 1/2 chance, putting in .25 would be a 1/4 chance.): ")
        try:
            _1 = int(evaltime)
            evaltime = int(evaltime)
        except:
            error = "Invalid evaluation time."
        try:
            _1 = int(breaktime)
            breaktime = int(breaktime)
        except:
            error = "Invalid break time."
        try:
            _1 = int(minimum)
            minimum = int(minimum)
            _1 = int(maximum)
            maximum = int(maximum)
            if maximum-minimum<=0:
                error = "Invalid push-ups amounts. (Make sure that max > min)"
        except:
            error = "Invalid push-ups amounts. (Make sure that max > min)"
        try:
            _1 = float(freq)
            if float(freq)>=0 and float(freq)<=1:
                freq = float(freq)
            else:
                error = "Invalid push-up frequency."
        except:
            error = "Invalid push-up frequency."
        if error=="":
            loop = False
            break

def wait(waittime,message,sec_message):
    t=int(waittime)-1
    if sec_message!="":
        msg="{0} -- {1}".format(message,sec_message)
    else:
        msg=message
    for x in range(int(waittime)):
        time=t
        if len(str(t))==1:
            time="0"+str(t)
        if not t==0:
            print(msg+" ({0})".format(str(time)), end="\r")
        else:
            print(message+" ({0}) Done!                                                                        ".format(str(time)))
        sleep(1)
        t-=1

i=0
pushups = 0
while True:
    print(Style.BRIGHT + Fore.GREEN)
    clear()
    print("You have done a total of {0} push-ups in this session.".format(str(pushups)))
    _1 = input("Press enter once you've completed a map.")
    
    print(Fore.CYAN)
    wait(evaltime,"Evaluate performance.","What were you good at? What were you bad at?")
    wait(breaktime,"Take a break.","Stand up and go outside!")
    wait(5,"Drink water","Hydration is good for stamina and your physical well-being.")

    if random()<=freq:
        pushup_amt = round((maximum-minimum)*random()+minimum)
        print(Fore.YELLOW)
        _2 = input("Surprise! Do {0} push-ups. (press enter when completed.)".format(str(pushup_amt)))
        print(Fore.GREEN)
        pushups+=pushup_amt
    sleep(1)
    i+=1
    