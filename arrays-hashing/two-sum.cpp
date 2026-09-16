// Idea: store each value and its index in a hash map. 
// For each num, look up its complement (target - num) in the map. 
// Brute force is O(n^2); hash lookup is O(1), so total is O(n*1) = O(n).
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;

        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int num = nums[i];

            if (mp.count(target - num) == 1){
                return {mp[target - num], i};
            }
            mp[num] = i;
        }
        return{};
    }
};
