num = int(input("Enter a number: "))

for i in range(1,num):
    if(num%i)== 0:
        print("number is not prime")
        break
else:
    print("Number is prime")    

