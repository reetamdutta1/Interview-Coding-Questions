a = ['my','full','name','is','reetam','dutta']

print(a[0]) #prints first item of the list
print(a[2]) #prints 3rd item of the list
print(a[len(a)-1]) #prints last item of list
print(a[-1]) #prints last item of list
print(a[-2]) #prints 2nd-last item of list
print("\n-----------------------------------\n")

# a[m:n] returns the portion of a:
# Starting with postion m
# Up to but not including n

print(a[2:5]) #prints 2nd to 4th index items
print(a[1:4]) #prints 1st to 3rd index items
print(a[-5:-2]) #prints 5th-last to 2nd-last
print("\n-----------------------------------\n")

# a[:n] starts slice at the beginning of the list
# a[m:] extends slice from the 1st index m to the end

print(a[:4]) #prints till 3rd index item
print(a[2:]) #prints from 2nd index to last item
print(a[0:5:2]) #prints every 2 steps
print(a[::-1]) #prints reverse of list

