def fibo(n):
    if n < 0:
        return("INVALID INPUT")
    elif n == 0:
        return 0
    elif n ==1 or n ==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
if __name__ =='__main__':
    output = []
    n = int(input())
    for n in range(0,n+1):
        output.append(fibo(n))
    print(output)




