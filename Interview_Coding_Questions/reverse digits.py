class Solution:
    	def reverse_digit(self, n):
		# Code here
            rev = 0
            while(n>0):
                a = n%10
                rev = rev*10 + a
                n//=10
                
            return rev

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends