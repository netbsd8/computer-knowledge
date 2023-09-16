#include "../base.h"

class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (maxHeap.size() == 0) {
            maxHeap.push(num);
            return;
        }

        if (num <= maxHeap.top()) {
            maxHeap.push(num);
            if ((maxHeap.size() - minHeap.size()) > 1) {
                int t = maxHeap.top();
                maxHeap.pop();
                minHeap.push(t);
            }
        } else {
            minHeap.push(num);
            if ((minHeap.size() - maxHeap.size()) > 1) {
                int t = minHeap.top();
                minHeap.pop();
                maxHeap.push(t);
            }
        }
        return;
        
        
    }
    
    double findMedian() {
        if (maxHeap.size() == 0 && minHeap.size() == 0)
            return 0;
        
        if (maxHeap.size() == minHeap.size())
            return (maxHeap.top() + minHeap.top()) / 2.0;
        
        if (maxHeap.size() > minHeap.size())
            return maxHeap.top();
        else
            return minHeap.top();
        
    }
    
private:
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */