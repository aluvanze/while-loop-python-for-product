
n=int(input("enter  number of times\n"))
for i in range(n):
 while n!=0:

    num = int(input("enter a number\n"))
    if num<0:
        print("*"*20)
        print(" *enter a positive number*")
        print("*" * 20)
        continue
    product=num*num
    print("the product:",product)
    break

 else:
    print("end")
