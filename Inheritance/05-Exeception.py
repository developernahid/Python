try:
    x=input("Enter a number:")
    x=int(x)
    print(100/x)
except ZeroDivisionError:
      print("Cannot divided by zero")
      
except ValueError:
    print("Enter valid number")
finally:
    print("Program Ended")