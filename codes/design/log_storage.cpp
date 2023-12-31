#include "../base.h"

class LogSystem {
public:
    LogSystem() {
        granularity_["Year"] = 4;
        granularity_["Month"] = 7;
        granularity_["Day"] = 10;
        granularity_["Hour"] = 13;
        granularity_["Minute"] = 16;
        granularity_["Second"] = 19;
        
    }
    
    void put(int id, string timestamp) {
        lookup_.emplace(timestamp, id);
    }
    
    vector<int> retrieve(string s, string e, string gra) {
        auto ns = s.substr(0, granularity_[gra]) + s_filter_.substr(granularity_[gra]);
        auto ne = e.substr(0, granularity_[gra]) + e_filter_.substr(granularity_[gra]);
        
        vector<int> result;
        auto end = lookup_.upper_bound(ne);
        auto start = lookup_.lower_bound(ns);
        for (auto it = start; it != end; it++) {
            result.emplace_back(it->second);
        }
        return result;
    }
    
private:
    string s_filter_ = "0001:01:01:00:00:00";
    string e_filter_ = "9999:12:31:23:59:59";
    unordered_map<string, int> granularity_;
    multimap<string, int> lookup_;
};


class LogSystem_map {
public:
    LogSystem_map() {
        granularity_["Year"] = 4;
        granularity_["Month"] = 7;
        granularity_["Day"] = 10;
        granularity_["Hour"] = 13;
        granularity_["Minute"] = 16;
        granularity_["Second"] = 19;
        
    }
    
    void put(int id, string timestamp) {
        lookup_.emplace(timestamp, id);
    }
    
    vector<int> retrieve(string s, string e, string gra) {
        auto ns = s.substr(0, granularity_[gra]) + s_filter_.substr(granularity_[gra]);
        auto ne = e.substr(0, granularity_[gra]) + e_filter_.substr(granularity_[gra]);
        
        vector<int> result;
        auto end = lookup_.upper_bound(ne);
        auto start = lookup_.lower_bound(ns);
        for (auto it = start; it != end; it++) {
            result.emplace_back(it->second);
        }
        return result;
    }
    
private:
    string s_filter_ = "0001:01:01:00:00:00";
    string e_filter_ = "9999:12:31:23:59:59";
    unordered_map<string, int> granularity_;
    map<string, int> lookup_;
};

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem obj = new LogSystem();
 * obj.put(id,timestamp);
 * vector<int> param_2 = obj.retrieve(s,e,gra);
 */