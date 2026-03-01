class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        placemap = {
            4: 'Thousand',
            7: 'Million',
            10: 'Billion'
        }
        ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        teens=["Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        out = []
        pos=1
        snum=str(num)
        snum="".join(reversed(list(snum)))
        l=len(snum)
        while pos<l+1:
            c=snum[pos-1]
            if pos%3==0:
                if c != '0':
                    out.append("Hundred")
                    out.append(ones[int(c)])
            if pos%3==1:
                nxt=pos+1
                group_nonzero = any(int(snum[p-1]) != 0 for p in range(pos, min(pos+3, l+1)))
                if nxt<l+1 and snum[nxt-1]=="1":
                    if pos in placemap and group_nonzero:
                        out.append(placemap[pos])
                    out.append(teens[int(c)])
                    pos+=2
                    continue
                if pos in placemap and group_nonzero:
                    out.append(placemap[pos])
                out.append(ones[int(c)])
            if pos%3==2:
                out.append(tens[int(c)])
            pos+=1
        return " ".join(reversed(list(o for o in out if o != "")))

sol=Solution()
print(sol.numberToWords(12345))
print(sol.numberToWords(1234567))
print(sol.numberToWords(int(input())))