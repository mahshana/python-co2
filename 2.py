a=0
b=1
n=int(input("enter the limit"))
if n<=0:
    print("enter the number\n")
elif n==1 :
    print(a)
elif a==2 :
    print(a)
    print(b)
else :
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)