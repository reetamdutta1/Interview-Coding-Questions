def chkPalindrome(str1):
    b = str1.lower()
    a = b[::-1]
    if a == b:
        return("It is a Palindrome")
    else:
        return("It is NOT a Palindrome")

if __name__ =='__main__':
    str1 = input()
    print(chkPalindrome(str1))
"""
this program works for both
string and integer inputs
"""


