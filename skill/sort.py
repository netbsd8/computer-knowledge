from typing import List


class Solution:
    # quick sorting solution: T(n) = T(n/2) + O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, k, 0, len(nums)-1)

    def quickSelect(self, nums, k, start, end):
        l, r = start, end
        mid = l + (r-l)//2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if start + k -1 <= r:
            return self.quickSelect(nums, k, start, r)
        if start + k - 1 >= l:
            return self.quickSelect(nums, k-(l-start), l, end)
        return nums[r+1]

# lambda function
# lambda arguments: expression
# contain only one expression. 
"""
C++'s Lambda

int main() {
    int outside_var = 5;

    auto lambda = [outside_var](int x) -> int {
        return x + outside_var;
    };

    std::cout << lambda(3) << std::endl;  // Outputs 8
    return 0;
}
"""
words = ["apple", "banana", "cherry", "date", "fig"]
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)
['banana', 'cherry', 'apple', 'date', 'fig']

f = lambda x, y: x + y
print(f(2, 3))  # Outputs: 5

# capture variables from the enclosing scope, 
# it retains a reference to that variable even if it's used outside that scope later on.
#  if the captured variable is mutable (like a list) and is modified after the lambda is defined, the lambda will see the changed value.
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)   # Returns a lambda that multiplies its input by 2
triple = multiplier(3)   # Returns a lambda that multiplies its input by 3

print(double(5))   # Outputs: 10
print(triple(5))   # Outputs: 15


