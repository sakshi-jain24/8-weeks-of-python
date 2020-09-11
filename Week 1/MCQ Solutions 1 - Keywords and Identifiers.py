import os
import time

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


score=0
screen_clear()
print("1) Which of the following is not valid variable name in Python?\nA. 11var\nB. var_name\nC. _var\nD. (var)")
ans=input("Enter your Choice:")
screen_clear()
if ans=="a" or ans=="A":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is A")
    print("Current Score:",score,"out of 5")

print("2) How many keywords are there in python 3.7?\nA. 32\nB. 35\nC. 31\nD. 33")
ans=input("Enter your Choice:")
screen_clear()
if ans=="b" or ans=="B" or ans=="35" or ans=="d" or ans=="D" or ans=="33":
    score+=1
    print("Correct.Python 3.7 has 33 keywords and Python 3.7.3 and above has 35 keywords.\nCurrent Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is B or D\nPython 3.7 has 33 keywords and Python 3.7.3 and above has 35 keywords.")
    print("Current Score:",score,"out of 5")

print("3) What is the maximum length of an identifier in python??\nA. 128\nB. 31\nC. 64\nD. None of the Above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is D")
    print("Current Score:",score,"out of 5")

print("4) Which one of the following will give an error in python?\nA. x=’Hello’\nB. true=0\nC. Var1=”@gmail”\nD. None of the Above")
ans=input("Enter your Choice:")
screen_clear()
if ans=="d" or ans=="D":
    score+=1
    print("Correct.Current Score:",score,"out of 5")
else:
    print("Wrong/Invalid Choice.Correct Option is D")
    print("Current Score:",score,"out of 5")

print("5) Which of the following statment is False?\nA. Variable names can be arbitrarily long.\nB. They can contain both letters and numbers.\nC. Variable name can begin with number.\nD. Variable name can begin with underscore.")
ans=input("Enter your Choice:")
screen_clear()
if ans=="c" or ans=="C":
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
