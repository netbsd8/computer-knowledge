#include "../base.h"

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL)
            return NULL;
        
        Node* dummy = head;

        // insert new nodes into the exited list 
        while (head) {
            Node* node = new Node(head->val);
            node->next = head->next;            
            head->next = node;
            head = node->next;
        }
        
        head = dummy;
        while (head && head->next) {
            if (head->random)
                head->next->random = head->random->next;
            head = head->next->next;
        }
        

        Node* newDummy = new Node(0);        
        Node* cur = newDummy;
        head = dummy;
        while (head) {
            cur->next = head->next;
            if (head->next)
                head->next = head->next->next;
            cur = cur->next;
            head = head->next;
        }
        
        return newDummy->next;        
    }
};