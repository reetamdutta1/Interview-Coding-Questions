def printFirstLast(arr):
    output = []
    output.append(arr[0])
    output.append(arr[-1])

    return output

if __name__ =='__main__':
    user = []
    n = int(input("Enter number of items: "))
    for i in range(n):
        ele = int(input())
        user.append(ele)
    print("Your list: ")
    print(user)
    print("first and last elements are: ")
    print(printFirstLast(user))






