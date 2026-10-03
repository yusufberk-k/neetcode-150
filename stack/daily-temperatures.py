# Daily Temperatures
# status: solo | retry: -
# note: used two parallel stacks (temps + indices); 
# one index stack is enough since temperatures[i] gives the value. if/else was redundant too, just while-pop then append

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        sti = []
        days = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            if len(st) == 0 or t <= st[-1]:
                st.append(t)
                sti.append(i)
            else:
                while len(st) != 0 and t > st[-1]:
                    st.pop()
                    days[sti[-1]] = i - sti[-1]
                    sti.pop() 
                st.append(t)
                sti.append(i)
        return days
