op=input("enter op ")
def a():
    a=float(input())
    b=float(input())
    sum=a+b
    print(sum)
def s():
     a=float(input())
     b=float(input())
     sum=a-b
     print(sum)
def m():
     a=float(input())
     b=float(input())
     sum=a*b
     print(sum)
def d():
     a=float(input())
     b=float(input())
     sum=a/b
     print(sum)
while True:
    if op=="a":
        a()
        break
    elif op=="s":
        s()
        break
    elif op=="m":
        m()
        break
    elif op=="d":
        d()
        break
    else:
        print("Not an op")
        op=input()
