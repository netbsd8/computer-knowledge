#include "../base.h"

class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        vector<vector<string>> ret;
        int len = paths.size();
        if (len == 0)
            return ret;
        unordered_map<string, vector<string>> m;
        
        for (auto path : paths) {
            istringstream is(path);
            string dir;
            string t;
            is >> dir;
            while (is >> t) {
                int pos = t.find_last_of('(');
                int strLen = t.size();
                string content = t.substr(pos+1, (strLen-1) - (pos+1));
                m[content].push_back(dir + '/' + t.substr(0, pos));
            }
        }
        
        for (auto i : m) {
            if (i.second.size() > 1)
                ret.push_back(i.second);
        }
        
        return ret;
    }
};