def replaceChr(str1,a,b):
    str2 = str1.replace(a,b)
    return str2

# { Driver Code Starts

if __name__ == '__main__':
        str1 = input("Enter your string: ")
        a = input("Input character to replace: ")
        b = input("Input New character: ")
        print("New string: ",replaceChr(str1,a,b))

# } Driver Code Ends


