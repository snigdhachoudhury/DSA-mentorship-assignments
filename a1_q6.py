#therefore, 56738->83765
n = int(input("enter a number : "))
reverse = 0
while n>0:
  r = n%10
  reverse=(reverse*10)+r
  n//=10
print("reverse is : ", reverse)
