def findLargest(n):
    user = []
    for i in range(n):
        ele = int(input())
        user.append(ele)

    user.sort(reverse=True)
    return('Largest number is: {}'.
                      format(user[0]) )

# { Driver Code Starts
if __name__ == '__main__':
        n = int(input())
        print(findLargest(n))
# } Driver Code Ends


