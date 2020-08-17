import random
number = random.randrange(1 , 5555555555555)
def firstDigit(n) : 
  
    # Remove last digit from number 
    # till only one digit is left 
    while n >= 10:  
        n = n / 10; 
      
    # return the first digit 
    return int(n)
thenum = firstDigit(number)
print(number)
if thenum % 2 == 0:
    print("First Digit is even")
else:
    print("First Digit is odd.")
