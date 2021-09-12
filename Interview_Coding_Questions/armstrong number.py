def armstrongNumber (n):
    # code here 
    a = int(n%10) #unit's place digit
    #print(a)
    b = int((n/10)%10) #ten's place digit
    #print(b)
    c = int(n/100) #100's place digit
    #print(c)
    
    if((a*a*a + b*b*b + c*c*c) == n):
        return "YES an Armstrong Number"
    else:
        return "NOT an Armstrong Number"

# { 
#  Driver Code Starts
if __name__ == '__main__': 
        n = int(input())
        print(armstrongNumber(n))
# } Driver Code Ends

