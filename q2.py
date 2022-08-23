def prime_func(val1,val2):
   # prime function
  list = []
  print("Prime number between", val1, "and", val2, "are:")
  for num in range(val1, val2 + 1):
     if num > 1:
         for i in range(2, num):
           if(num%i) == 0:
             break
         else:
            list.append(num)
  print(list)

while True:
    # checking the input exception
    try:
        lower = int(input("1st Positive Value ="))
        upper = int(input("2st Positive Value ="))
    except ValueError:
        print("This is an unaccepted response, Enter a valid value")
        break
    else:
        if lower<1:
            print("Value Entered is less then 0, Enter a Value > 1")

        elif upper<1:
            print("Value Entered is less then 0, Enter a Value > 1")

        elif lower>upper:
            print("Enter correct positive range")

        elif lower == upper:
            print("Enter correct positive range")

        else:
            # calling function after checking exception
            prime_func(lower,upper)
            break