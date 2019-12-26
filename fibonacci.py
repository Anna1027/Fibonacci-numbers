#fn = fn -1 +fn+2
a = 0
b = 1

x = int(input("Enter the number: "))

if x < 0:
    print("invalid number")

elif x == 0:
    b=a

else:
    for i in range(2, x+1):
        c=a+b
        a=b
        b=c
print("The output fibonacci number: ", b)

