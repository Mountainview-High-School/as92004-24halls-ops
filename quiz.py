import time
user_name=input("What is your name ")
time.sleep(1)
print("Hello "+user_name+"")
time.sleep(1)
age = int(input("What is your age "))
if age >= 14:
  print("Sorry you aren't in the right age group for this quiz")
if age <= 7:
  print("Sorry you aren't in the right age group for this quiz")

#all instructions on how this quiz works
else:
 time.sleep(2)
 print("Welcome to this quiz you are going to be ask 3 qustions")
 time.sleep(2)
 print ()
 print("Ever time you get a qustion right on your frist try you will get a point")
 time.sleep(3)
 print ()
 print("you will have 3 chances to get the question right if you dont get it right you will be told the answer.")
 time.sleep(2)
 print ()
 print ("Your score is currently 0")
 time.sleep(2)
print()
sumbit = input ("write anything to say you understand ")
print()


question = ["Q1 Someone sends you a text that is hurtful and makes you feel bad about yourself. "
"A.Delete the message and try to forget about it "
"B.Keep the text and how an adult you trust"
"C.Text the person back saying something mean to them"]
correct_answer = ["B"]
for i in question :
 answer = input ()





