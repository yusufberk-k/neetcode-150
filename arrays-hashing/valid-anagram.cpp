// Idea: Compare the character frequencies of both strings using a single hash map.
// Increment the count for each char in s, decrement for each char in t,
// and erase a key once its count hits zero.
// If the map ends up empty, the strings are anagrams.
// This reduces time complexity to O(n), compared to sorting both strings (O(n log n)).
// Time: O(n)

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mp;
        int s_size = s.size();
        int t_size = t.size();

        if (s_size != t_size){
            return false;
        }
        
        for (int i = 0; i < s_size; i++) {
            char sc = s[i];
            char tc = t[i];
            mp[sc]++;
            mp[tc]--;
            if (mp[sc] == 0){
                mp.erase(sc);
            }
            if(mp[tc] == 0){
                mp.erase(tc);
            }
        }
        return mp.size() == 0;
    }
};
