#include "../base.h"

class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size(), cur = 0;
        int i = 0, j = 0;
        while (i < n) {
            while (j < n && chars[j] == chars[i])
                j++;
            chars[cur] = chars[i];
            cur ++;
            if (j - i != 1) {
                for (char c : to_string(j - i))
                    chars[cur ++] = c;
            }
            i = j;
        }

        return cur;
    }
};