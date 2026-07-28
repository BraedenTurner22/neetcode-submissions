class KthLargest {

private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    int k;

public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        for (const int& n : nums) {
            add(n);
        }
    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size() > k) {
            pq.pop();
        }
        return pq.top(); 
    }
};
