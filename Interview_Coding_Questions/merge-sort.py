def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_2_sorted_lists(left,right)

def merge_2_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1

        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


if __name__ == '__main__':
    user = []
    n = int(input("Enter number of items: "))
    for i in range(n):
        ele = int(input())
        user.append(ele)

    print(merge_sort(user))
