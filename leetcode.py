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
    def partitionString(self,s: str) -> int:
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
   def buildArray(self, target: List[int], n: int) -> List[str]:
       """
        You are given an integer array target and an integer n.
        
        You have an empty stack with the two following operations:
        
        "Push": pushes an integer to the top of the stack.
        "Pop": removes the integer on the top of the stack.
        You also have a stream of the integers in the range [1, n].
        
        Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:
        
        If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
        If the stack is not empty, pop the integer at the top of the stack.
        If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
        Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.
        
         
        
        Example 1:
        
        Input: target = [1,3], n = 3
        Output: ["Push","Push","Pop","Push"]
        Explanation: Initially the stack s is empty. The last element is the top of the stack.
        Read 1 from the stream and push it to the stack. s = [1].
        Read 2 from the stream and push it to the stack. s = [1,2].
        Pop the integer on the top of the stack. s = [1].
        Read 3 from the stream and push it to the stack. s = [1,3].
        Example 2:
        
        Input: target = [1,2,3], n = 3
        Output: ["Push","Push","Push"]
        Explanation: Initially the stack s is empty. The last element is the top of the stack.
        Read 1 from the stream and push it to the stack. s = [1].
        Read 2 from the stream and push it to the stack. s = [1,2].
        Read 3 from the stream and push it to the stack. s = [1,2,3].
        Example 3:
        
        Input: target = [1,2], n = 4
        Output: ["Push","Push"]
        Explanation: Initially the stack s is empty. The last element is the top of the stack.
        Read 1 from the stream and push it to the stack. s = [1].
        Read 2 from the stream and push it to the stack. s = [1,2].
        Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
        The answers that read integer 3 from the stream are not accepted.
         
        
        Constraints:
        
        1 <= target.length <= 100
        1 <= n <= 100
        1 <= target[i] <= n
        target is strictly increasing.
       """
        count=0
        output = []
        for value in target:
            count += 1
            while count < value:
                output.extend(['Push', 'Pop'])
                count += 1
            output.append('Push')
        return output
