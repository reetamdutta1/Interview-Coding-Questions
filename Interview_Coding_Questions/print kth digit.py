"""
Example 1:

Input:
A = 3
B = 3
K = 1
Output:
7
Explanation:
33 = 27 and 1st
digit from right is 
7
"""

class Solution:
    def kthDigit(self, A, B, K):
        # code here
        x = pow(A,B)  #calculate A^B
        temp = 0
        while(K>0):  #find k-th digit from right
            temp = x%10 #getting the last digit
            x = x//10
            K -=1
            
        return temp
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B,K = input().split()
        ob = Solution()
        print(ob.kthDigit(int(A),int(B),int(K)))
# } Driver Code Ends