# question on conditional's
# 1) Age group categorization
# Classify a person's age group : Child(<13), Teeneager(13 - 19),Adult(20-59),(senior(60 +))

# age = int(input("Enter you'r age: "))
# if age <= 12:
#   print('You are child!')
# elif age >= 13 and age <= 19:
#   print('You are teenager!')
# elif age >= 20 and age <= 59:
#   print('You are adult!')
# else:
#   print('You are Senior!')

# 2) Movie Ticiket Pricing 
# The Prices of Movie Ticikets Based on age : 12$ for adult's(18 and over) , 
# 8$ for Children . Everyone get's a 2$ discount on wednesday

# age = int(input('Enter your age:  '))
# which_Day = input('Which Day is Today!!').lower()
# if age >= 18 and which_Day != 'Wednesday'.lower():
#   print("There will be 12$ Only!!")
# elif age <= 12 and which_Day != 'Wednesday'.lower():
#   print("There will be 10$ Only!!")
# elif age >= 18 and which_Day == 'Wednesday'.lower():
#   print("There will be 10$ Only!!, 2% Discount!")
# elif age <= 17 and which_Day == 'Wednesday'.lower():
#   print('There will be 8$ Only !! 2% Discount!')


# 3)Grade Calculator
# Assign a Letter grade based on student's Score :A (90-100), B(80 - 89)
# C(70 - 79), D(60 - 69),F


# grade = int(input("Enter You're Grade:  "))
# if grade >= 90 and grade <= 100:
#   print("You are A Grade Student!!")
# elif grade >= 80 and grade <= 89:
#   print("You are B Grade Student!!")
# elif grade >= 70 and grade <= 79:
#   print("You are C Grade Student!!")
# elif grade >= 60 and grade <= 69:
#   print("You are D Grade Student!!")
# else:
#   print("You are F Grade Student!!")  # grade < 60


# 4)Fruit Ripeness Checker
# Determine if a fruit is ripe, overripe or unripe based on it's color 
# (eg Bananna : Green - Unripe, Yellow : Ripe , Brown - Overripe)


# which_fruit = input('which fruit is this: ').lower()
# color_of_fruit = input("what is the color of the fruit?: ").lower()
# if color_of_fruit == 'green':
#   print(f'The {which_fruit} is still Unripe!')
# elif color_of_fruit == 'yellow':
#   print(f'The {which_fruit} is ripe!')
# elif color_of_fruit == 'brown':
#   print(f'The {which_fruit} is Overripe!')
# else:
#   print(f"The {color_of_fruit} is Not Recocnizable !! Try Again ")


# 5) Weather Activity Sugestion 
# Suggest an Activity based on the weather (eg, Sunny-Go for a walk ,Rainy -Read a book, Snowy - Build a Snowman)


# weather_checking = input('How is Weather Today??: ')
# if weather_checking.lower() == 'sunny':
#   print('Go For a Walk Then It will be good for you !!')
# elif weather_checking.lower() == 'rainy':
#   print('Stay Home and Do some programming!!!')
# elif weather_checking.lower() == 'snowy':
#   print('Go Skiing or Build a Snowman!!')

# 6) Transportation Mode Selection
# Choose a mode of Transport Based on the distance (eg.<3km: Walk)(3 - 15 km : Bike)(>15 km : car)

# Distance = int(input('Enter Distance: '))
# if Distance <=3:
#   print('Walk')
# elif Distance >=4 and Distance <= 15:
#   print('Bike')
# else:
#   print('Car')  # Distance > 15

# 7) Coffee Customization
# Customize an Coffee Order: "Small" "Medium" and "Large" with an Option for "Extra shot " of Espresso

# size = input('How Big You Want the size of coffee: ').lower()
# coffee_Enquiery = input('Do You Want An Extra Shot of Espresso!: ').lower()
# if size == 'small' and  coffee_Enquiery == 'yes':
#   print('You will get a small coffee with an extra shot of espresso!!')
# elif size == 'small' and coffee_Enquiery == 'no':
#   print('You will get a small coffee!!')
# if size == 'medium' and  coffee_Enquiery == 'yes':
#   print('You will get a medium coffee with an extra shot of espresso!!')
# elif size == 'medium' and coffee_Enquiery == 'no':
#   print('You will get a medium coffee!!')
# if size == 'large' and  coffee_Enquiery == 'yes':
#   print('You will get a large coffee with an extra shot of espresso!!')
# elif size == 'large' and coffee_Enquiery == 'no':
#   print('You will get a large coffee!!')  


# 8) password strength checker
# check if password is strong , medium or weak less than 6 means weak, 6 to 10 character's mean's medium , 
# more than 10 character's then strong 


# print('******************Password Strength Checker***************************')
# password = input('Enter the password: ')
# if len(password) < 6:
#   print('Password is too short. Please choose a longer password.')
# elif len(password) >= 6 and len(password) <= 11:
#   print('Password is Medium.')
# elif len(password) > 12:
#   print('Password is Strong!!')  # Password is strong if it is more than 12


# 9)Leap year checker
# Determine if year is a leap year .(Leap year's are divisible by 4 , but no by 100 unless also divisible by 400)



# print('**************************Leap Year checker****************************')
# year = int(input('Enter a Year: '))
# if year % 4 == 0 and year % 100 != 0:
#   print('Year is a Leap Year')
# elif year % 400 == 0:
#   print('Year is not a Leap Year')
# else:
#   print('Year is not a Leap Year')  

# 10) Pet food Recomandation
# Recommend a type of pet food based on the pet's specie's and age 
# e.g(Dog: < 2 yesr's - puppy food , Cat > 5 yesr's - Senior Cat food)


# print("*********************Pet Food Recomendation*************************************")
# animal = input('what is your pet: ')
# age = int(input('Enter the age of the pet: '))
# if age <= 2:
#   print('Give Puppy Food!')
# elif age >= 2:
#   print('Give Senior Food!')