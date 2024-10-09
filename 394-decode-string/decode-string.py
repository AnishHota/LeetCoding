class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for x in s:
            if x!=']':
                stack.append(x)
            else:
                st = ""
                while stack and stack[-1]!='[':
                    st =  stack.pop()+st
                stack.pop()
                num=''
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                num_i = int(num)
                stack.append(num_i*st)
                
        return ''.join(stack)