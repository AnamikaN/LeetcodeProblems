# Write a function to find the longest common prefix string amongst an array of strings. If there is no
# common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non - empty.
from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    longest_common_prefix = LongestCommonPrefix()
    strs = ["flower", "flow", "flight"]
    result = longest_common_prefix.longestCommonPrefix(strs)
    print(result == "fl")

    strs = ["dog","racecar","car"]
    result = longest_common_prefix.longestCommonPrefix(strs)
    print(result == "")