
#n = input("Enter a number: ")
#factorial = 1
 
#for i in range (1,int(n)+1):
#       factorial = factorial * i
 
#print(factorial)

#answer = []
#for i in str(factorial):
#    answer.append(i)
#print(f"factorial of {n} is {answer}")

## attempted after discussed.

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
number = int(input("Enter number: "))

list=[]
total = str(fact(number))
for num in total:
    list.append(num)

print(','.join(list))
