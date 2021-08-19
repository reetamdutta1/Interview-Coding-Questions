
def fibo(n):
    fib=[0,1] #initial values

    for i in range(2,n):
        next_num = fib[-1]+fib[-2]  #adding last two numbers in the list

        fib.append(next_num) #adding the new sum in the list
    return fib

N = int(input("Enter number of terms for fibonacci series: "))
fib=fibo(N) #return fibonacci list upto first n terms
print(fib)


