numbers = [1, -3, 2, -4,5, 9, 10, -32, -45]

positive_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1

print("Positive numbers count =", positive_count)


#While Loop

i= int(input("Enter the value of i: "))
while(i<38):
    i=int(input("Enter the value of i:"))
    print(i)
if(i>38):
    print("Enter the smaller value of i:")
else:
     print("Done with the loop")   



n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)







while True:
    i = int(input("Enter the value of i: "))
    print(i)

    if i <= 38:
        print("Value is <= 38")

    elif i > 45:
        print("Done with the loop")
        break

    else:
        print("Enter smaller value of i")

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)



number=9
for i in range (2,11):
    if i==11:
        break
    print(number,'X',i,'=',number*i)




def multiply(a, b):
    
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    
    
    elif isinstance(a, str) and isinstance(b, int):
        return a * b
    elif isinstance(b, str) and isinstance(a, int):
        return b * a
    
    else:
        return "Invalid input"



print(multiply(3, 5))        
print(multiply("8", 3))     
print(multiply(4, "5"))      
print(multiply("7", "A"))   


