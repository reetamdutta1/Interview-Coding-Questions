def oddEvenSum(n):
    odd = []
    even = []
    for i in range(n):
        ele = int(input())
        if ele%2 == 0:
            even.append(ele)
        else:
            odd.append(ele)
    print("Sum of even numbers: ", sum(even))
    return("Sum of odd numbers: {}".format(sum(odd)))

# { Driver Code Starts
if __name__ == '__main__':
        n = int(input())
        print(oddEvenSum(n))
# } Driver Code Ends


    