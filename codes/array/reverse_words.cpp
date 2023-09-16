#include "../base.h"

class Solution {
public:
    string reverseWords(string s) {
        stringstream sm(s);
        vector<string> words;
        string temp;
        while (sm >> temp) {
            words.push_back(temp);
        }

        string ret = "";
        for (auto rit=words.rbegin(); rit != words.rend(); ++rit) {
            ret = ret + *rit + " ";
        }

        return ret.substr(0, ret.size()-1);
    }
};

/*
python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ret = " ".join(words[::-1])
        return ret
        
*/