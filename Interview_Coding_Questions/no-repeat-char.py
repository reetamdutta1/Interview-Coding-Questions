def noRepeatChar(string):
    from collections import Counter
    freq = Counter(string)
    for i in string:
        if freq[i]==1:
            return i
            #coming out of loop

# { Driver Code Starts
if __name__ == '__main__':
        str1 = input()
        print(noRepeatChar(str1))
# } Driver Code Ends

