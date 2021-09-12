def find2ndLargest(n):
    user = []
    new_list = []

    for i in range(n):
        ele = int(input())
        user.append(ele)

    new_list = set(user) #to get distinct values
    print(new_list)
    new_list.remove(max(new_list))
    return('2nd Largest number is: {}'.format(max(new_list)) )

# { Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
        n = int(input())
        print(find2ndLargest(n))
# } Driver Code Ends
