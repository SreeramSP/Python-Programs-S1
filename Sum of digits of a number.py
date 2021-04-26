num = int(input("Enter the number="))
sum = 0 
temp = num
while temp > 0:
  digit = temp % 10
  sum = sum + digit
  temp //= 10
print(sum)