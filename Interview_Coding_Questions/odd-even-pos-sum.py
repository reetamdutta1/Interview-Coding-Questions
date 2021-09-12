def oddEvenPos(n):
    user = []      #Pos - 1 2 3 4 5 6 7 . . .
    oddPos = 0     #List [9 5 7 4 1 3 6 . . .]
    evenPos = 0    #Index 0 1 2 3 4 5 6 . . .
    for i in range(n):      #   ^^
        ele = int(input())  #   ||
        user.append(ele)    #see here

    for a in range(1, len(user),2):
        evenPos = evenPos + user[a]
    for b in range(0, len(user),2):
        oddPos = oddPos + user[b]
    

    print("Odd position sum: {}".format(oddPos))
    return "Even position sum: {}".format(evenPos)
    
if __name__ =='__main__':
    n = int(input())
    print(oddEvenPos(n))

#odd sum = 9+7+1+6 = 23
#even sum = 5+4+3 = 12


