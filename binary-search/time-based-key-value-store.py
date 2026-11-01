# Time Based Key-Value Store
# status: solo | retry: -
# note: retry passed, dict.setdefault(key, []).append(...) creates the list on first use and appends in one line;
# set timestamps are strictly increasing so each key's list stays sorted -> get = binary search for the
# largest ts <= target: save the value whenever mt <= target and go right, O(log n) get

class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        self.vals = self.keys.get(key, [])
        l, r = 0, len(self.vals)-1

        pa = ''
        while l <= r:
            m = l + (r-l)//2
            lt = self.vals[l][1]
            mt = self.vals[m][1]
            mv = self.vals[m][0]

            if mt <= timestamp:
                pa = mv
                l = m+1
            
            else:
                r = m-1
        return pa
