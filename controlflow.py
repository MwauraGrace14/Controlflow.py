#Control flow with If/else and conditional operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height>= 120:
  print("You can have a ride on the rollercoaster!")
  age = int(input("What is your age?"))
  if age<12:
    print("Child pay $7")
    bill = 7
  elif age<= 18:
    print("Teenage pay $10")
    bill = 10
  elif age>=45 and age<=55:
    print("Have a free ride on us!")
  else:
    print("Adult pay $12")
    bill = 12
  wants_photo = input("Do yo want a photo taken? Y or N. ")
  if wants_photo=="Y":
    bill +=3
    print(f"Yourfinal bill is {bill}")
else:
  print("Grow taller!")
  
  
#Practical exercise

number = int(input("Enter a number "))

remainder = number % 2
if remainder >0:
    print("This is an odd number.")
else:
    print("This is an even number.")


#Example2


height = float(input("Enter your height"))
weight = int(input("Enter your weight"))
a = height
b = weight
bmi = round(b/a**2 ,1)
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")

else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#Leap Year
  
year = int(input("Enter the year"))
if year%4 ==0:
  print(f"{year} is a leap year")
  if year%100 ==0:
    print(f"{year} is a leap year")
    if year%400 ==0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not leap year")
  else:
    print(f"{year} is not leap year")
else:
  print(f"{year} is not leap year")
  
