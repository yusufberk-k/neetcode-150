# Car Fleet
# status: solo | retry: -
# note: sorted() returns a new list, use .sort() for in-place; don't ceil arrival times, 2.5 and 3.0 are different fleets

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        steps = {}
        st = []

        for i in range(len(position)):
            step = (target - position[i]) / speed[i]
            steps[position[i]] = step

        position.sort()

        fleets = 0
        for s in reversed(position):
            if len(st) == 0 or st[0] >= steps[s]:
                st.append(steps[s])
            else:
                while(len(st) != 0):
                    st.pop()
                fleets += 1
                st.append(steps[s])
        if len(st) != 0:
            fleets += 1

        return fleets
