# Recursive
- O(2^n)
# O(1)
# O(logn)
- T(n) = T(n/2) + O(1) = T(n/4) + O(1) + O(1) = T(n/8) + O(1) + O(1) + O(1) = T(1) + log(n) * O(1)
- binary search
- binary tree may not be log(n) depend on structure
# O(sqrt(n))
# O(n)
- T(n) = T(n/2) + O(n) = T(n/4) + O(n/2) + O(n) = T(n/8) + O(n/4) + O(n/2) + O(n) = T(1) + O(2n) = O(n)
# O(nlogn)
- quick sort
  - T(n) = 2T(n/2) + O(n) = 2(2T(n/4) + O(n/2)) + O(n) = 4T(n/4) + O(n) + O(n) = 8(T/8) + 3*O(n) = T(1) + logn * O(n) = O(nlogn)
  - T(n) = 2T(n/2) + O(1) = 2(2T(n/4) + O(1)) + O(1) = 4T(n/4) + O(2) + O(1) = T(1) + O(1+2+4+...+n) = O(2n)
# O(n^2) - O(n^3)
- array, enumerate, dp
# O(2^n)
- combination
# O(n!)
- permutation