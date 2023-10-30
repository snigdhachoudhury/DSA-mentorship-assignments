print("enter input:" )
n=int(input())

op=1
inv=0
while n>0:

    od=n%10

    np=od
    nd=op

    mult=pow(10,np-1)
    inv=inv+nd*mult

    op=op+1
    n=n//10
print(inv)
