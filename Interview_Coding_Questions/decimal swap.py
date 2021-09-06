def swap(num):
    num = str(float(num))
    a,b = num.split('.')
    res = b + '.' + a
    return res

# { Driver Code Starts
if __name__ == '__main__':
        n = input()
        print(swap(n))
# } Driver Code Ends



