# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if: Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class ValidParentheses:
    def isValid(self, s: str) -> bool:
        opcl = { '(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for idx in s:
            if idx in '([{':
                stack.append(idx)
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False

        return len(stack) == 0

if __name__ == "__main__":
    valid_parentheses = ValidParentheses()

    result = valid_parentheses.isValid("()")
    print(result == True)

    result = valid_parentheses.isValid("()[]{}")
    print(result == True)

    result = valid_parentheses.isValid("(]")
    print(result == False)

    result = valid_parentheses.isValid("([])")
    print(result == True)