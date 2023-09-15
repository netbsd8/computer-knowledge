#include "../base.h"

class Logger {
public:
    Logger() {}
 
    bool shouldPrintMessage(int timestamp, string message) {
        while (!msg.empty() && timestamp-msg.front().second >= 10) {
            table.erase(msg.front().first);
            msg.pop();
        }
        if (table.find(message) != table.end()) {
            return false;
        } else {
            table[message] = timestamp;
            msg.push(make_pair(message, timestamp));
            return true;
        }
    }
private:
    unordered_map<string, int> table;
    queue<pair<string, int>> msg;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */