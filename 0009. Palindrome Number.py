def isPalindrome(self, x):
        if x<0: return False
        div= 1
        while x>10*div:
            div*=10
        while x:
            right= x%10