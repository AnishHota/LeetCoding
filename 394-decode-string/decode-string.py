class Solution:
    def decodeString(self, s: str) -> str:
        sSt = False
        num = ''
        stack = []
        st = []
        ans = ''
        for x in s:
            if x!=']':
                stack.append(x)
            else:
                while stack and stack[-1]!='[':
                    st.append(stack.pop())
                st = st[::-1]
                string = ''.join(st)
                stack.pop()
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                num = num[::-1]
                num_i = int(num)
                stack.append(num_i*string)
                num=''
                st = []
                
        return ''.join(stack)