print("Thank you for downloading this calculator!")
print("Calculator - Created by Autum")
print("Please enter your first value.")
a = int.input("First value: ")
print("Please enter your second value.")
b = int.input("Second value: ")
print("Please select an oporation:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")
c = int.input("Operation: ")
if c == 1:
  result = print(a+b)
elif c == 2:
 result = print(a-b)
elif c == 3:
 result = print(a*b)
elif c == 4:
 result = print(a/b)
else:
  result = print("Sorry, but I cannot recognize that value."), go to 7
print("Is there anything else I can do for you?\n 1. Yes\n 2. No")
