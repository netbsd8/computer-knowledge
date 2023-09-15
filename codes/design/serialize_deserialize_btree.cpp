#include "../base.h"

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class S_D_Btree_Recursive {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        ser_helper(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream in(data);
        return des_helper(in);
    }
    
private:
    void ser_helper(TreeNode* root, ostringstream& out) {
        if (root) {
            out << root->val << " ";
            ser_helper(root->left, out);
            ser_helper(root->right, out);
        } else {
            out << "# ";
        }
    }
    
    TreeNode* des_helper(istringstream& in) {
        string val;
        if (!(in >> val))
            return nullptr;
        if (val == "#")
            return nullptr;
        TreeNode* node = new TreeNode(stoi(val));
        node->left = des_helper(in);
        node->right = des_helper(in);
        
        return node;
    }
};

class S_D_Btree {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        ostringstream out;
        if (!root)
            return out.str();
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* t = q.front();
            q.pop();
            if (t) {
                out << t->val << ' ';
                q.push(t->left);
                q.push(t->right);
            } else {
                out << "# ";
            }
        }
        
        return out.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int n = data.size();
        if (n == 0)
            return nullptr;
        istringstream in(data);
        
        string val;
        in >> val;      
        TreeNode* root = new TreeNode(stoi(val));
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* t = q.front();
            q.pop();
            
            if (!(in >> val))
                break;
            if (val != "#") {
                TreeNode* left = new TreeNode(stoi(val));
                t->left = left;
                q.push(left);
            }
            
            if (!(in >> val))
                break;
            if (val != "#") {
                TreeNode* right = new TreeNode(stoi(val));
                t->right = right;
                q.push(right);
            }
        }
        
        return root;                                                                                                    
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));