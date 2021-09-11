def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]: #swapping done here
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__ =='__main__':
    user = []
    n = int(input("Enter number of integers: "))
    for i in range(n):
        ele = int(input())
        user.append(ele)
    bubbleSort(user)
    print("The bubble-sorted array is: ")
    print(user)




