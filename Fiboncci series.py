total = int(input("Total Fibonacci Numbers to be printed="))
n1, n2 = 0, 1
count = 0
if total <= 0:
   print("Please enter a positive integer")
elif total == 1:
   print("Fibonacci sequence upto",total,"=")
   print(n1)
else:
   print("Fibonacci sequence=")
   while count < total:
       print(n1)
       n = n1 + n2
       n1 = n2
       n2 = n
       count = count + 1