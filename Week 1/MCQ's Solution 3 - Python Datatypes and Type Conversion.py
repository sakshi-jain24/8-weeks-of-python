import os
import time

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


score=0
screen_clear()
print("1) Which of the following are used to convert the string into the list?\nA. scanner()\nB. lambda()\nC. convertor()\nD. split()")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is D")
    print("Current Score:",score,"out of 5")

print("2) Which of the following is not the data type in python?\nA. tuple\nB. class\nC. set\nD. list")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B" or ans=="Class" or "class":
    score+=1
    print("Correct. Class is not a data type in Python.\nCurrent Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is B")
    print("Current Score:",score,"out of 5")

print("3) Which of the following is the example of the type casting?\nA. str(2)\nB. int(2)\nC. str(list)\nD. All of the Above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is D")
    print("Current Score:",score,"out of 5")

print("4) Which of the following can convert the string to float number?\nA. str(float,x)\nB. float(str,int)\nC. int(float(str))\nD. float(str)")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is C")
    print("Current Score:",score,"out of 5")

print("5) If we change one data type to another, then it is called?\nA. Type Conversion\nB. Type Casting\nC. Both of the Above\nD. None of the Above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="c" or ans=="C":
    score+=1
    print("Correct.Your Total Score is:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is C")
    print("Your Total Score is:",score,"out of 5")
if (score>=3):
    print("Congratulation! You secured",(score/5)*100,"%.")
else:
    print("You secured",(score/5)*100,"%. You need more practice.")

time.sleep(10)