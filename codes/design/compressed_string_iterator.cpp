#include "../base.h"

class StringIterator {
public:
    StringIterator(string compressedString) {
        s = compressedString;
        length = s.size();
        index = 0;
        cnt = 0;
        c = ' ';
    }
    
    char next() {
        if (hasNext()) {
            cnt --;
            return c;
        }
        return ' ';
    }
    
    bool hasNext() {
        if (cnt > 0)
            return true;
        else {
            if (index >= length)
                return false;
            
            c = s[index];
            index ++;
            while (index < length && s[index] >= '0' && s[index] <= '9') {
                cnt = cnt * 10 + s[index] - '0';
                index ++;
            }
            return true;        
        }
    }
    
private:
    string s;
    int length, index, cnt;
    char c;
};

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator obj = new StringIterator(compressedString);
 * char param_1 = obj.next();
 * bool param_2 = obj.hasNext();
 */