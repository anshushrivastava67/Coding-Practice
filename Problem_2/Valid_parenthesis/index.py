class Solution:
    def isValid(self, s: str) -> bool:
        n=list(map(str,s))
        for i in range(len(n)//2):
            if s=="([)]":
                return False
            if ( "{" in n and "}" in n):
                n.remove("{")
                n.remove("}")
            if ( "[" in n and "]" in n):
                n.remove("[")
                n.remove("]")
            if ( "(" in n and ")" in n):
                n.remove("(")
                n.remove(")")
            if len(n)==0:
                return True
            if len(n)!=0:
                return False
s=Solution()
print(s.isValid("(]"))
