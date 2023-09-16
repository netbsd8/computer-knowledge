#include "../base.h"

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (beginWord == endWord)
            return 1;
        
        int count = 0;
        unordered_set<string> us;
        unordered_set<string> dicts;
        for (auto word: wordList) {
            dicts.insert(word);
        }
        
        queue<string> q;
        q.push(beginWord);
        us.insert(beginWord);
        
        while (!q.empty()) {
            int len = q.size();
            count += 1;
            for (int i = 0; i < len; i++) {
                string cur = q.front();
                q.pop();
                
                vector<string> words = getNextWords(cur, dicts);
                for (auto word : words) {
                    if (word == endWord)
                        return count + 1;
                    if (us.count(word) != 0)
                        continue;
                    q.push(word);
                    us.insert(word);
                }
            }
        }
        
        return 0;
    }
    
private:
    vector<string> getNextWords(string word, unordered_set<string>& dicts) {
        vector<string> ret;
        for (char i = 'a'; i <= 'z'; i++) {
            for (int j = 0; j < word.size(); j++) {
                if (i == word[j])
                    continue;
                char t = word[j];
                word[j] = i;
                if (dicts.count(word))
                    ret.push_back(word);
                word[j] = t; 
            }
        }
        return ret;
    }
};