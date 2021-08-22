"""
You are given four numbers num1,
den1, num2, and den2. You need to
find (num1/den1)+(num2/den2) and
output the result in the form of
(numx/denx).
"""

def addFraction(num1, den1, num2, den2):
    #Code here
    from math import gcd
    num = num1*den2+num2*den1
    den = den1*den2
    ka=gcd(num,den)
    h=num//ka
    d=den//ka
    print(str(h)+"/"+str(d))

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))
        addFraction(arr[0], arr[1], arr[2], arr[3])

# } Driver Code Ends