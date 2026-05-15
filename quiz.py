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
 time.sleep(1)
 print ()
 print("Ever time you get a qustion right on your frist try you will get a point")
 time.sleep(1)
 print ()
 print("you will have 3 chances to get the question right if you dont get it right you will be told the answer.")
 time.sleep(1)
 print ()
 print ("Your score is currently 0")
 time.sleep(1)



question = ["Q1 Someone sends you a text that is hurtful and makes you feel bad about yourself. ",
"A.Delete the message and try to forget about it ",
"B.Keep the text and how an adult you trust",
"C.Text the person back saying something mean to them",
"Q2 You find out that someone has posted an embarrassing picture of you online. ",
"A.Tweet that they are an idiot and a loser ",
"B.Ask your friends to give the person a hard time",
"C.Tell an adult you trust",
"Q3 You want to join an online gaming site. Which of the following information is okay for you to post on the site.",
"A. A Nickname",
"B. Your name",
"C. Email address"]
correct_answer = ["B","C","A"]
i = 0
while i < len(question):
 print(question[i])
 time.sleep(1)
 print(question[i+1])
 time.sleep(1)
 print(question[i+2])
 time.sleep(1)
 print(question[i+3])
 answer = input ("")
 print(correct_answer[int(i/4)])
 time.sleep(1)
 i += 4


# print(question[i+4])
#time.sleep(1)
#print(question[i+5])
#time.sleep(1)
#print(question[i+6])
#time.sleep(1)
#print(question[i+7])
#answer = input ("")
# 0 1 2 3 4 5 6 7 8 9 10




