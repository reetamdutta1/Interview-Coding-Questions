#input:  5 9 6 7 8 2 4 3
#output: 6 8 2 4 5 9 7 3

def oddAfterEven(arr):
    #initialize left & right indexes
    left, right = 0, len(arr)-1

    while left<right:
        #increment left index
        while arr[left]%2 == 0 and left<right:
            left += 1

        #decrement right index
        while arr[right]%2 ==1 and left<right:
            right -= 1

        if (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

if __name__ =='__main__':
    n = int(input())
    user =[]
    for i in range(n):
        ele = int(input())
        user.append(ele)

    print(oddAfterEven(user))
