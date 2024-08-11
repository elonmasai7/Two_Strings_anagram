class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0
        for char in count_s:
            if count_s[char] > count_t[char]:
                steps += count_s[char] - count_t[char]


        return steps

solution = Solution()

s1, t1 = "bab", "aba"
s2, t2 = "leetcode", "practice"
s3, t3 = "anagram", "mangaar"

print(solution.minSteps(s1, t1))
print(solution.minSteps(s2, t2))
print(solution.minSteps(s3, t3))
