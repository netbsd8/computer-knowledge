#include "../base.h"

class LRUCache {
public:
    LRUCache(int capacity) : capacity_(capacity) {
        
    }
    
    int get(int key) {
        if (m_.find(key) == m_.end()) {
             return -1;
        }

        auto pos = m_[key];
        int val = (*pos)[1];
        l_.erase(pos);
        l_.push_front({key, val});
        m_[key] = l_.begin();

        return val;
    }
    
    void put(int key, int value) {
        if (m_.find(key) == m_.end()) {
            if (l_.size() < capacity_) {
                l_.push_front({key, value});
                m_[key] = l_.begin();                 
            } else {
                auto del_pos = l_.back();
                int del_key = del_pos[0];
                m_.erase(del_key);
                l_.pop_back(); 

                l_.push_front({key, value});
                m_[key] = l_.begin(); 
            }

        } else {
            auto pos = m_[key];
            l_.erase(pos);
            l_.push_front({key, value});
            m_[key] = l_.begin();            
        }
        
    }

private:
    unordered_map<int, list<vector<int>>::iterator> m_;
    list<vector<int>> l_;
    int capacity_;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */