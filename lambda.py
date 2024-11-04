numbers = int(input("Enter your number"))
square = lambda num: num * num
print(square(numbers))

#######
numbers = int(input("Enter your number"))
check_even = lambda num : num % 2
if check_even(numbers) == 0:
    print("That number is even")
else:
    print("That number is odd")
