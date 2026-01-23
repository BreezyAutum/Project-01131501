print("Calculator - Created by Autum\t\nThank you for downloading this calculator!\t\nPlease enter your first value.")
a = input("First value: ")
print("Please enter your second value.")
b = input("Second value: ")
print("Please select an oporation:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5, Exponent")
c = input("Operation: ")
c = float(c)
a = float(a)
b = float(b)
if c == 1:
 print(a + b)
elif c == 2:
 print(a - b)
elif c == 3:
 print(a * b)
elif c == 4:
 print("Which type?\n 1. True Divsion\n 2. Remainder")
 d = input("Operation: ")
 d = int(d)
 if d == 1:
   print("True Divion: ", a / b)
 elif d == 2:
   d = print("Quotient:", a // b, "\nRemainder:", a % b)
 else:
  print("Sorry. I cannot understand what you typed.")
elif c == 5:
 print(a ** b)
else:
  print("Sorry, but I cannot recognize that value.")
print("Thank you. Have a good day! :D")