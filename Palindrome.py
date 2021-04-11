n=int(input("Enter the number="))
temp=n
b=0
while(n>0):
  a=n%10
  b=b*10+a
  n=n//10
if(temp==b):
  print("It is palindrome")
else:
  print("It is not palindrome")  