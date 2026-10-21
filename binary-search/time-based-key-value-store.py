# Time Based Key-Value Store
# status: hint | retry: 2026-10-28
# note: set timestamps are strictly increasing, so appending keeps each key's list sorted (no insort needed);
# get = binary search for the largest timestamp <= target: save the value whenever ts < target and go right

class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key] = self.keys.get(key, [])
        self.keys[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ''
        self.ts = self.keys[key]
        
        l, r = 0, len(self.ts)-1
        
        ans = ''
        while l <= r:
            m = l + (r-l)//2
            self.mt = self.ts[m][0]

            
            if self.mt == timestamp:
                return self.ts[m][1]
            
            elif self.mt < timestamp:
                ans = self.ts[m][1]
                l = m+1
            
            else: 
                r = m-1
            
        return ans