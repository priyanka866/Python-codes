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
print(a)
weight = float(input("Enter your weight in kg"))
print(b)
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


# In[ ]:




