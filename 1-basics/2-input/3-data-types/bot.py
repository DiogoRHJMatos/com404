print("\nWhat is your name human?")

name = input()

print("\nHow old are you (in years)?")

age = int(input())

print("\nHow tall are you (in meters)?")

height = float(input())

print("\nHow much do you weigh (in kilograms)?")

weight = float(input())

bmi = weight / (height * height)

print("\n" + name + " you are " + str(age) + " years old and your bmi is " + str(bmi) + ".")