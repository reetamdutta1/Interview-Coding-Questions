def charCount(str1,a):
    str1 = str1.lower()
    a = a.lower()
    b = str1.count(a)
    return b

# { Driver Code Starts
if __name__ == '__main__':
        str1 = input()
        n = input()
        print(charCount(str1,n))
# } Driver Code Ends

