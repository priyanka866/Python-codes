#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Print function
print('What to print')
print('print("What to print")')
print('print("What to print")\nAnything')
print("Hello "+ "priyanka")
print("Day 1- String Manipulation")
print('String Concatention is done through "+" sign.\ne.g. print("Hello" + "world")')
print("New lines can be created with a backslash and n.")
a=input("What is your name?")
print(len(a))


# In[22]:


#input function
city = input("What is the name of your city?")
print(a)
pet = input("What is the name of your pet?")
print(b)
print("Your band name is",city,pet)

#Type eroor and type conversion 
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
type(street_name)

#Adding two digit by user input
a = input("Enter two digit number ")
c= int(a[0])+ int(a[1])
print(c)

#BMI calculator
height= float(input("Enter your height in m"))
weight = float(input("Enter your weight in kg"))
BMI = weight/height**2
print("Your BMI is",BMI)


# In[62]:


#Number of days left until 90 from current age 
curr_age = int(input("What is your current age?"))
rem_age = 90 - curr_age
print(f"Remmaing age until 90: {rem_age} years")
days = int((365*rem_age))
weeks = int((52*rem_age))
months = int((12*rem_age))
print(f"You have {days} days,{weeks} weeks and {months} months left.")

#Tip Calculator
bill = float(input("What was the total bill? "))
tip =  float(input("What percent tip would u like to give? "))
tip_amt = bill*float(tip/100)
print(f"Tip added: {tip_amt}")
Tot_bill = bill+ tip_amt
print(f"Total bill : {Tot_bill}")
split = int(input("How many people are there to split the bill "))
amt_pay = round(Tot_bill/split,2)
amt_pay = "{:.2f}".format(amt_pay)
print(f"Each person should pay : {amt_pay}")
#or reduce variable 
amt_pay1 =  round((bill+(bill*float(tip/100)))/split,2)
print(f"Each person should pay : {amt_pay1}")


# In[6]:


#If else statement
user_in = int(input("Enter number to test odd or even "))
if user_in % 2==0:
    print("Number is even")
else:
    print("Number is odd")
    
#BMI calculator
height= float(input("Enter your height in m "))
weight = float(input("Enter your weight in kg "))
BMI = weight/height**2
print(f"Your BMI is: {BMI}")
if BMI < 18.5:
    print("You are underweight")
elif 18 < BMI < 25:
    print("You are normal weight")
elif 25 < BMI < 30:
    print("You are overweight")
elif 30 < BMI < 35:
    print("You are obese")
else:
     print("You are clinically obese")

#Leap year
year = int(input("Enter the year "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
elif year % 400 == 0:
     print(f"{year} is a leap year")        
else:
    print(f"{year} is not a leap year")
    
#Pizza order program

size = input("What size pizza do you want? [S, M, L] ")
add_pepperoni = input("Do you want pepperoni? [Y, N] ")
extra_cheese = input("Do you want extra cheese? [Y, N] ")

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

#Love Calculator
name1 = "Mohit"
name2 = "Priyanka"
concat = name1 + name2
lower_names = concat.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e


l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

love_scores = int(str(first_digit)+ str(second_digit))

print(f"Your score is {love_scores}")
if love_scores <10 or love_scores > 90:
    print(f"Your score is {love_scores}, you go together like coke and mentos.")
elif 40 < love_scores < 50:
    print(f"Your score is {love_scores}, you are alright together.")    
else:
     print(f"Your score is {love_scores}")


# In[7]:


#treassure game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure choosing.") 

path = input("Where do you want to go? [left/right] ").lower() 


if path == "left":
    next_path = input("What do you want to do? [swim/wait] ").lower()
    if next_path =='wait':
       third_path = input("Which door you want to go? [red/blue/yellow] ").lower() 
       if third_path == 'red':
        print("Burned by fire..\n Game Over.")
       elif third_path == 'blue':
        print("Eaten by beasts.\n Game Over. ")
       elif third_path == 'yellow':
        print("You win! ")
       else:
            print("Game over")
    elif next_path =='swim':
         print("Attached by a beast.\n Game Over. ")

else:
    print("Fall into a hole.\n Game Over. ")


# In[45]:


#Random module
import random

rand_number = random.randint(0,1)

if rand_number == 1:
    print("Heads")
else:
    print("Tail")
    
#Bill split

import random
people = input("Enter the name to split the bill- ")
plp_split= people.split(", ") #Angela, Ben, Jenny, Michael, Chloe
print(plp_split)
##bill_pay = random.choice(plp_split) 
random_pay = random.randint(0,(len(plp_split)-1))
bill_pay = plp_split[random_pay]
print(f"{bill_pay} will pay the bill today")

#treasure map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")


# In[93]:


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_in = int(input("What will you choose? 0 for rock,1 for paper, 2 for scissors "))
comp_in = random.randint(0,2)

if user_in < 0 and user_in >3:
    print("Invalid number")
else:
    game = [rock,paper,scissors]
    print(game[user_in])
    print(game[comp_in])

    if user_in == 0 and user_in == 2:
      print("You win!")
    elif comp_in == 0 and user_in == 2:
      print("You lose")
    elif comp_in > user_choice:
      print("You lose")
    elif user_in > comp_in:
      print("You win!")
    elif comp_in == user_in:
      print("It's a draw")


# In[ ]:





# In[ ]:




