# try except block - try catch block

class NegativeError(Exception):
  pass
  

try:
  n = int(input("Enter a numerator: "))
  d = int(input("Enter a denomenator: "))

  if n < 0 or d < 0:
    raise NegativeError("No Negative numbers please")

  q = n/d

  print(q)

except ZeroDivisionError:
  print("Denominator cannot be zero")

except ValueError:
  print("Please type numbers only")

except NegativeError:
  print("Please don't input negative numbers")

except Exception as e:
  print(e)
  print("Something went wrong!!")

else:
  # Whenever try block is successfully executed without throwing any exceptions
  print("I am else block")

finally:
  #this will run at the end weather any error was thrown or not
  print("I am finally block")

print("End of the program")

# file handling example
# try
  # open a file
  # try to do something
  # write into the file - it may throw error 
# except
  # do something to handle the error
# finally
  # close the file