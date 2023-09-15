#include "../base.h"

class FileSystem {
public:
    FileSystem() : root_(new TrieNode()) {
        
    }
    
    vector<string> ls(string path) {
        auto curr = getNode(path);
        
        if (curr->isFile)
            return {split(path, '/').back()};
        
        vector<string> result;
        for (const auto& child : curr->children) {
            result.emplace_back(child.first);
        }
        
        sort(result.begin(), result.end());
        return result;
    }
    
    void mkdir(string path) {
        auto curr = putNode(path);
        curr->isFile = false;
    }
    
    void addContentToFile(string filePath, string content) {
        auto curr = putNode(filePath);
        curr->isFile = true;
        curr->content += content;
    }
    
    string readContentFromFile(string filePath) {
        auto curr = getNode(filePath);
        if (curr)
            return curr->content;
        return "";
    }
    
private:
    struct TrieNode {
        bool isFile;
        unordered_map<string, TrieNode*> children;
        string content;
    };
    
    TrieNode* root_;
    
    vector<string> split(const string& s, const char delim) {
        vector<string> tokens;
        stringstream ss(s);
        string token;
        
        while(getline(ss, token, delim)) {
            if (!token.empty())
                tokens.emplace_back(token);
        }
        
        return tokens;
    }
    
    TrieNode* getNode(const string& path) {
        vector<string> strs = split(path, '/');
        auto curr = root_;
        for (const auto& str : strs) {
            curr = curr->children[str];
        }
        
        return curr;
    }
    
    TrieNode* putNode(const string& path) {
        vector<string> strs = split(path, '/');
        auto curr = root_;
        for (const auto& str: strs) {
            if (!curr->children.count(str))
                curr->children[str] = new TrieNode();
            curr = curr->children[str];
        }
        return curr;
    }
    
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * vector<string> param_1 = obj->ls(path);
 * obj->mkdir(path);
 * obj->addContentToFile(filePath,content);
 * string param_4 = obj->readContentFromFile(filePath);
 */