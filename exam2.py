
n=int(input("enter  number of times\n"))


for i in range(n):
 while n!=0:

    num1= int(input("Enter First Number\n"))
    num2 = int(input("Enter Second number\n"))
    if num1<0 or num2<0:
        print("*"*20)
        print(" *enter a positive number*")
        print("*" * 20)
        break
    product=num1*num2
    print("the product:",product)
    break

 else:
    print("end")
