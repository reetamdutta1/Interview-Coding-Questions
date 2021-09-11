num = int(input())
lst = []
count = 0

for i in range(2, num+2):
    for j in range(2,i):
        if i%j ==0:
            break
        else:
            lst.append(i)

sum = lst[0]
for j in range(1,len(lst)):
    sum = sum + lst[j]

if sum in lst:
    count += 1

print(count)