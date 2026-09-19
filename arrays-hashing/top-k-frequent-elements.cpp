// Approach 1: Max-heap (initial solution)
// Time: O(n + m log m), worst case O(n log n) | Space: O(n)
// n = nums.size(), m = number of distinct elements
// Count frequencies, push all (freq, num) pairs into a max-heap, pop k times.

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        priority_queue<pair<int,int>> q;
        vector<int> maxFreq;
        for (int i : nums) freq[i]++;
        
        for (auto [i, v] : freq) {
            q.push({v, i});
        }

        for (int i = 0; i < k; i++) {
            maxFreq.push_back(q.top().second);
            q.pop();
        }

        return maxFreq;
    }
};

// Approach 2: Bucket sort (optimal)
// Time: O(n) | Space: O(n)
// Key idea: a frequency can be at most n, so use it as an index.
// bucket[f] holds all numbers that appear exactly f times.
// Traverse buckets from high to low until k elements are collected.

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        vector<int> maxFreqs;
        vector<vector<int>> bucket(nums.size() + 1);
        
        for (int i : nums) freqs[i]++;
        
        for (auto [num, freq] : freqs) bucket[freq].push_back(num);

        for (int f = nums.size(); f > 0 && maxFreqs.size() < k; f--) {
            for (int num : bucket[f]) {
                maxFreqs.push_back(num);
                if (maxFreqs.size() == k) break;
            }
        }
        return maxFreqs;
    }
};
