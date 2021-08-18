#Input:
#N = 13 , M = 4
#Output:
#12
#Explanation:
#12 is the Closest Number to
#13 which is divisible by 4.


#User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        # code here 
        q=int(N/M)
        n1 = q*M #1st closest number
         # 2nd possible closest number
        if((N * M) > 0) :
            n2 = (M * (q + 1))
        else :
            n2 = (M * (q - 1))
        if(abs(N-n1)<abs(N-n2)):
            return n1
        return n2
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        
        ob = Solution()
        print(ob.closestNumber(N,M))
# } Driver Code Ends