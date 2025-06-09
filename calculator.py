print("Welcome to calculator")
history=[]
while True:
  try :
      num1=float(input("Enter 1st number:"))
      print(f"{num1}\n")
      sign=input("Enter the sign(+/-/*/÷):")
      print(f"{sign}\n")
      num2=float(input("Enter 2nd number:"))
      print(f"{num2}\n")
      if sign=="+":
            num3 = num1 + num2
      elif sign=="-":
            num3 = num1 - num2
      elif sign=="*":
            num3 = num1 * num2 
      elif sign=="÷" or sign=="/": 
       if num2==0:
           print("Error")
       else:
           num3 = num1 / num2
      else: 
          print("Error , Invalid sign")
          num3 = None
  except ValueError :
      print("Error , Invalid input")
  if num3 is not None:   
      print(f"final answer is:{num3}\n")
  result_str = f"{num1}{sign}{num2}={num3}" 
  history.append(result_str) 
  user = input("Q to quit , H to history , any other key to use calculator") 
  if user.upper()=="H":
        print("History of calculations:")
        for item in history:
            print(item)
  elif user.upper()=="Q":
      print("thank you for using the calculator")
      break