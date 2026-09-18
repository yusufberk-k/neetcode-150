class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, int> seen;
        vector<vector<string>> groups;

        for (string s : strs) {
            map<char, int> freq;
            for (char c : s) freq[c]++;

            if (!seen.count(freq)) {
                seen[freq] = groups.size();
                groups.push_back({});
            }
            groups[seen[freq]].push_back(s);
        }
        return groups;
    }
};
