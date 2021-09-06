def primeRange(a,b):
    output = []
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if num%i ==0:
                    break
            else:
                output.append(num)
    return (output)


# { Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
        n = int(input())
        p = int(input())
        print(primeRange(n,p))
# } Driver Code Ends