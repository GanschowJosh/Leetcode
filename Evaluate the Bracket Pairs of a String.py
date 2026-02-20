import re
class Solution:
    def evaluate(self, s, knowledge) -> str:
        k=dict(knowledge)
        out=[]
        l = len(s)
        i=0
        while i < l:
            curr=s[i]
            if curr != '(': out.append(curr); i+=1;continue
            j=i+1
            tocheck=[]
            while j < l:
                t=s[j]
                if t==')':
                    tocheck="".join(tocheck)
                    #print(tocheck)
                    if tocheck in k: out.append(k[tocheck])
                    else: out.append("?")
                    i=j+1
                    break
                tocheck.append(t)
                j+=1
        return("".join(out))
sol=Solution()
print(sol.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]))