print("Please enter the first whole number.")

fir = int(input())

print("Please enter the second whole number.")

sec = int(input())

print("Please enter the third whole number.")

tir = int(input())

even = 0
odd = 0

if(fir % 2 == 0):
    even = even + 1
else:
    odd = odd + 1

if(sec % 2 == 0):
    even = even + 1
else:
    odd = odd + 1

if(sec % 2 == 0):
    even = even + 1
else:
    odd = odd + 1

print("There are " + str(even) + " evens and " + str(odd) + " odds.")