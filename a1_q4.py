n=int(input())
for i in range(2,n+1):
  isPrime=True
  j=2
  while j<1:
    if i%j==0:
        isPrime=False
        break
    j=j+1
  if isPrime:
    print(i)
      
