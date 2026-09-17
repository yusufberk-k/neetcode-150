// Idea: Store the numbers already visited in a hash map (num -> count).
// For each num, increment its count; if it exceeds 1, it's a duplicate.
// This reduces time complexity from O(n^2) (brute force) to O(n).
// Note: a hash set would be a better fit since only presence matters, not counts.
// I used a hash map here by choice.
// Time: O(n), Space: O(n)


class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int num : nums) {
            mp[num]++;
            auto it = mp.find(num);
            if (it->second > 1) {
                return true;
            }
        }
        return false;
    }
};