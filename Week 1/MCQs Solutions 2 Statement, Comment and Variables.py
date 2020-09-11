import os
import time

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


score=0
screen_clear()
print("1. Which of the following symbol are used for comment in python\nA.# \nB.\" " " \nC.Option 1 and 2 \nD.None of the above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="c" or ans=="C":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is C")
    print("Current Score:",score,"out of 5")

print("2) Most of the programming languages like C, C++, and Java use braces { } to define a block of code. Python, however, uses ____. \nA.Indentation \nB.Semi-Colon \nC.Parentheses\nD.4.None of the above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="a" or ans=="A" :
    score+=1
    print("Correct.Most of the programming languages like C, C++, and Java use braces { } to define a block of code. Python, however, uses Indentation.\n Current Score://",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is A\n  Most of the programming languages like C, C++, and Java use braces { } to define a block of code. Python, however, uses Indentation")
    print("Current Score:",score,"out of 5")

print("3) Which of the following will give error?\nA. a=b=c=1 \nB. a,b,c=1 \nC. a,b,c=1, \"Hello\", 1.5 \n D.None of the above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is B")
    print("Current Score:",score,"out of 5")

print("4) Which one of the following is correct way of declaring and initialising a variable, x with value 5 ?\nA. int x  x=5 \nB. int x=5 \nC. x=5 \nD.declare x=5")
ans=input("Enter your Choice:")
screen_clear()
if ans=="c" or ans=="C":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is C")
    print("Current Score:",score,"out of 5")

print("5)In Python, a variable must be declared before it is assigned a value:\nA. True \nB.False")
ans=input("Enter your Choice:")
screen_clear()
if ans=="a" or ans=="A":
    score+=1
    print("Correct.Your Total Score is:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is A")
    print("Your Total Score is:",score,"out of 5")
if (score>=3):
    print("Congratulation! You secured",(score/5)*100,"%.")
else:
    print("You secured",(score/5)*100,"%. You need more practice.")

time.sleep(10)
