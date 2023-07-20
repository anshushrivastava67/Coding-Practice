class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        special={'IX':9,'XL':40,'CM':900,'XC':90,'IV':4,'CD':400}
        sum=0
        i=0
        
        while i<len(s):
            if i+1<len(s) and s[i:i+2] in special:
                sum+=special[s[i:i+2]]
                i+=2
            else:
                sum=sum+a[s[i]]
                i+=1

        return sum

s=Solution()
print(s.romanToInt("IX"))
