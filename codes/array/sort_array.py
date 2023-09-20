from typing import List
import random

# Quick sort
class Solution_Quick:
    def threeWayPartition(self, x, low, high, pivot):
        x[low], x[pivot] = x[pivot], x[low]
        i, lt, gt = low, low, high
        while i <= gt and i < len(x) and gt >= 0:
            if x[i] < x[lt]:
                x[i], x[lt] = x[lt], x[i]
                i += 1
                lt += 1
            elif x[i] > x[lt]:
                x[i], x[gt] = x[gt], x[i]
                gt -= 1
            else: # x[i] == x[lt]
                i += 1
        return lt, gt

    def sortArray(self, nums: List[int], low=0, high=None) -> List[int]:
        if high is None:
            high = len(nums) - 1
        
        if len(nums) <= 1 or high <= low:
            return nums

        pivot = random.randint(low, high)
        lt, gt = self.threeWayPartition(nums, low, high, pivot)
        self.sortArray(nums, low, lt - 1)
        self.sortArray(nums, gt, high)
        return nums

# Merge sort
"""
Complexity Analysis
Here, nnn is the number of elements in the nums array.

Time complexity: O(nlog⁡n)O(n \log n)O(nlogn)

We divide the nums array into two halves till there is only one element in the array, which will lead to O(log⁡n)O(\log n)O(logn) steps.
n→n/2→n/4→...→1 (k steps)n \rarr n/2 \rarr n/4 \rarr ... \rarr 1 \space (\text{k steps})n→n/2→n/4→...→1 (k steps)
n/2(k−1)=1  ⟹  n / 2^{(k-1)} = 1 \impliesn/2 
(k−1)
 =1⟹ k≈log⁡nk \approx \log nk≈logn
And after each division, we merge those respective halves which will take O(n)O(n)O(n) time each.
Thus, overall it takes O(nlog⁡n)O(n \log n)O(nlogn) time.
Space complexity: O(n)O(n)O(n)

The recursive stack will take O(log⁡n)O(\log n)O(logn) space and we used an additional array temporaryArray of size nnn.
Thus, overall we use O(log⁡n+n)=O(n)O(\log n + n) = O(n)O(logn+n)=O(n) space.

"""


class Solution_Merge:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp_arr = [0] * len(nums)
        
        # Function to merge two sub-arrays in sorted order.
        def merge(left: int, mid: int, right: int):
            # Calculate the start and sizes of two halves.
            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            # Copy elements of both halves into a temporary array.
            for i in range(n1):
                temp_arr[start1 + i] = nums[start1 + i]
            for i in range(n2):
                temp_arr[start2 + i] = nums[start2 + i]

            # Merge the sub-arrays 'in tempArray' back into the original array 'arr' in sorted order.
            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else:
                    nums[k] = temp_arr[start2 + j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < n1:
                nums[k] = temp_arr[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1

        # Recursive function to sort an array using merge sort
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            # Sort first and second halves recursively.
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            # Merge the sorted halves.
            merge(left, mid, right)
    
        merge_sort(0, len(nums) - 1)
        return nums

# Heap sort
class Solution_Heap:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Function to heapify a subtree (in top-down order) rooted at index i.
        def heapify(n: int, i: int):
            # Initialize largest as root 'i'.
            largest = i;
            left = 2 * i + 1
            right = 2 * i + 2
            # If left child is larger than root.
            if left < n and nums[left] > nums[largest]:
                largest = left
            # If right child is larger than largest so far.
            if right < n and nums[right] > nums[largest]:
                largest = right
            # If largest is not root swap root with largest element
            # Recursively heapify the affected sub-tree (i.e. move down).
            if largest != i:
                nums[i], nums[largest] =  nums[largest], nums[i]
                heapify(n, largest)

        def heap_sort():
            n = len(nums)
            # Build heap; heapify (top-down) all elements except leaf nodes.
            for i in range(n // 2 - 1, -1, -1):
                heapify(n, i)
            # Traverse elements one by one, to move current root to end, and
            for i in range(n - 1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                # call max heapify on the reduced heap.
                heapify(i, 0)

        heap_sort()
        return nums

# Counting sort
class Solution_Count:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            # Create the counting hash map.
            counts = {}
            # Find the minimum and maximum values in the array.
            minVal, maxVal = min(nums), max(nums)
            # Update element's count in the hash map.
            for val in nums:
                counts[val] = counts.get(val, 0) + 1

            index = 0
            # Place each element in its correct position in the array.
            for val in range(minVal, maxVal + 1, 1):
                # Append all 'val's together if they exist.
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    counts[val] -= 1

        counting_sort()
        return nums

# Radix sort
class Solution_Radix:
    # Radix sort function.
    def radix_sort(self, nums: List[int]) -> List[int]:
        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for val in nums:
            max_element = max(abs(val), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        place_value = 1
        
        # Bucket sort function for each place value digit.
        def bucket_sort():
            buckets = [[] for i in range(10)]
            # Store the respective number based on it's digit.
            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                buckets[digit].append(val)

            # Overwrite 'nums' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        # Radix sort, least significant digit place to most significant.      
        for _ in range(max_digits):
            bucket_sort()
            place_value *= 10

        # Seperate out negatives and reverse them. 
        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        # Final 'arr' will be 'negative' elements, then 'positive' elements.
        return negatives + positives
            
    def sortArray(self, nums: List[int]) -> List[int]:  
        return self.radix_sort(nums)      
