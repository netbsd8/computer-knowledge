#include "../base.h"

class Solution {
public:
    int totalNQueens(int n) {
        vector<int> col;
        int ans = 0;
        solveNQ(ans, col, n, 0);
        return ans;
    }
    
    void solveNQ(int& ans,
                 vector<int>& col,
                 int nums, int curRow)
    {
        if (curRow == nums)
        {
            ans++;
            return;
        }
            
        for (int curCol=0; curCol<nums; curCol++)
        {
            if (isValidP(col, curRow, curCol))
            {
                col.push_back(curCol);
                solveNQ(ans, col, nums, curRow+1);
                col.pop_back();
            }
        }
    }
    
    bool isValidP(vector<int>& col, int curRow, int curCol)
    {
        for (int i=0; i<col.size(); i++)
        {
            if (col[i] == curCol || (abs(curRow-i) == abs(curCol - col[i])))
                return false;
        }
        return true;
    }
};