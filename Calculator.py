print("Thank you for downloading this calculator!")
print("Calculator - Created by Autum")
print("Please enter your first value.")
a = input("First value: ")
print("Please enter your second value.")
b = input("Second value: ")
print("Please select an oporation:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5, Exponent")
c = input("Operation: ")
c = int(c)
a = int(a)
b = int(b)
if c == 1:
 print(a + b)
elif c == 2:
 print(a - b)
elif c == 3:
 print(a * b)
elif c == 4:
 print("True division:", a / b, "\nQuotient:", a // b, "\nRemainder:", a % b)
elif c == 5:
 print(a ** b)
else:
  print("Sorry, but I cannot recognize that value.")
print("Thank you. Have a good day! :D")