# Program to send if the number is power of 4 or not

# Take input 
n = int(input("Enter your number : "))

def checkIfPower(n):
     # If n is less than equal to 0 just say no 
     if(n<=0):
          return False
     # if we reach lowest power of n just return true 
     if (n==1):
          return True 
     if(n%2==0):
          return checkIfPower(n/2)
     return False

if(checkIfPower(n)):
     print("Power of 2")
else:
     print("Not power of 2")