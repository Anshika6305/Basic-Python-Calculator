a=int(input("Enter any number: "))
b=int(input("Enter another number: "))
c=input("Enter the operaation sign: ")
if(c=="+"):
    print("Addition of given number is: ",a+b)
elif(c=="-"):
    print("subtraction of given number is: ",a-b)
elif(c=="*"):
    print("Multiplication of given number is: ",a*b)
elif(c=="/"):
    print("Division of given number is: ",a/b)
else:
    print("OOPS! Somthing Went Wrong.........")
