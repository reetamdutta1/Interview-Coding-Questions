#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here 
        a = int(n%10)
        b = int((n/10)%10)
        c = int(n/100)
        
        if((a*a*a + b*b*b + c*c*c) == n):
            return "Yes"
        else:
            return "No"

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends