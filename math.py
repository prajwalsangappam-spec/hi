try:
  a = float(input("enter first number :"))
  b = float(input("enter second number :"))
  
  print(f"Addition :{a+b}")
  print(f"substraction :{a-b}")
except ValueError:
  print("please enter valid number.")
