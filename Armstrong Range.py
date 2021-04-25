lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for num in range(lower,upper + 1):
   sum = 0 
   order = len(str(num))
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)


