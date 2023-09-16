#include "../base.h"

 // Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* kNode = getKthNode(head, k);
        if (kNode) {
            ListNode* nextHead = reverseKGroup(kNode->next, k);
            reverseList(head,k);
            head->next = nextHead;
            return kNode;
        }
        else {
            return head;
        }
    }
    
    ListNode* reverseList(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        /*
        ListNode* last = head;
        for (int i = 1; i < k; i++) {
            if (!last)
                return head;
            last = last->next;
        }
        */
        
        ListNode* prev = NULL;
        ListNode* cur = head;
        ListNode* t = NULL;
        while (k > 0) {
            t = cur->next;
            cur->next = prev;
 
            prev = cur;
            cur = t;
            
            k--;
        }
        dummy->next = prev;
        
        return dummy->next;
    }
    
    ListNode* getKthNode(ListNode* head, int k) {
        while (k > 1 && head) {
            head = head->next;
            k --;
        }
        
        if (k > 1)
            return NULL;
        return head;
    }
};