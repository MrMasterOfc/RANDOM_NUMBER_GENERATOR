import random


def phoneNumber(operator):
  endNum = random.randint(10000000,99999999)
  number = f"01{operator}{endNum}"
  print(number)

print('''
       CHOISE YOUR OPERATOR
       [1] GRAMEENPHONE
       [2] ROBI
       [3] BANGLALINK
''')
choise = input("Enter your choise: ")
amount = int(input("Amoumt of numbers: "))
if choise == '1':
  for i in range(amount+1):
    phoneNumber(7)
elif choise == '2':
  for i in range(amount+1):
    phoneNumber(8)
elif choise == '3':
    for i in range(amount+1):
      phoneNumber(9)
else:
  print("Wrong input")
    