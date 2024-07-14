class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        ans = ""
        i = 0
        n = len(formula)
        elem = ""
        stack.append(defaultdict(int))
        curr_dig = 0
        while i<n:
            if formula[i]=="(":
                stack.append(defaultdict(int))
            elif formula[i]==")":
                curr_dig = ""
                while i+1<n and formula[i+1].isnumeric():
                    curr_dig += formula[i+1]
                    i+=1
                curr_dig = 1 if not curr_dig else int(curr_dig)
                curr_has = stack.pop()
                prev_has = stack[-1]
                for elem in curr_has:
                    prev_has[elem] += curr_has[elem]*curr_dig
            else:
                curr_dig = ""
                elem = formula[i]
                if i+1<n and formula[i+1].islower():
                    elem += formula[i+1]
                    i = i+1
                while i+1<n and formula[i+1].isnumeric():
                    curr_dig += formula[i+1]
                    i+=1
                curr_has = stack[-1]
                curr_has[elem] += 1 if not curr_dig else int(curr_dig)
            i+=1
        
        has = stack[-1]
        for elem in sorted(has.keys()):
            count = "" if has[elem]==1 else has[elem]
            ans += elem + str(count)
        return ans
        

        