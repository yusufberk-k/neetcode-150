# Evaluate Reverse Polish Notation
# status: hint | retry: 2026-10-09
# note: // floors toward -inf (-7 // 2 = -4), problem wants truncation toward zero, so use int(a / b)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for n in tokens:
            if n == '+':
                s1 = st[-2] + st[-1]
                st.pop()
                st.pop()
                st.append(s1)

            elif n == '-':
                s2 = st[-2] - st[-1]
                st.pop()
                st.pop()
                st.append(s2)
            
            elif n == '*':
                s3 = st[-2] * st[-1]
                st.pop()
                st.pop()
                st.append(s3)
                
            elif n == '/':
                s4 = int(st[-2] / st[-1])
                st.pop()
                st.pop()
                st.append(s4)
                
            else:
                st.append(int(n))

        return st[-1]
