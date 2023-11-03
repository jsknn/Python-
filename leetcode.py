class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
 

Constraints:

1 <= k <= n <= 1000
 

Follow up:

Could you solve this problem in less than O(n) complexity?
"""
        factors=[]
        for i in range(1,n+1):
            if n%i==0:
                factors.append(i)
        if len(factors)>=k:
            return factors[k-1]
        else:
            return -1
        
"""
Leetcode best answer
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorCnt = 0
        for x in range(1, n + 1):
            if n % x == 0:
                factorCnt += 1
            if factorCnt == k:
                return x
        return -1
"""
    def partitionString(s: str) -> int:
        """
        Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
    
    Return the minimum number of substrings in such a partition.
    
    Note that each character should belong to exactly one substring in a partition.
    
     
    
    Example 1:
    
    Input: s = "abacaba"
    Output: 4
    Explanation:
    Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
    It can be shown that 4 is the minimum number of substrings needed.
    Example 2:
    
    Input: s = "ssssss"
    Output: 6
    Explanation:
    The only valid partition is ("s","s","s","s","s","s").
     
    
    Constraints:
    
    1 <= s.length <= 105
    s consists of only English lowercase letters.
        """
        empty_set = set()
        ans = 1
        for character in s:
            if character in empty_set:
                #incrementing 1 if charcter is present
                ans += 1
                # again making the set empty
                empty_set = set()
            #adding the charcter to the set for comparision with next character    
            empty_set.add(character)
        return ans
