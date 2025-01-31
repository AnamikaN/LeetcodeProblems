class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber*10 + x%10
            x //= 10
        return x == revertedNumber or x == revertedNumber //10

if __name__ == "__main__":
    palindrome_number_instance = PalindromeNumber()

    result = palindrome_number_instance.isPalindrome(121)
    print(result)

    result = palindrome_number_instance.isPalindrome(5335)
    print(result)

    result = palindrome_number_instance.isPalindrome(1)
    print(result)

    result = palindrome_number_instance.isPalindrome(10)
    print(result)

    result = palindrome_number_instance.isPalindrome(-12)
    print(result)