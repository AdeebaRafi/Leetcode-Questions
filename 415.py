class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1  # start from last digit of num1
        j = len(num2) - 1  # start from last digit of num2
        carry = 0
        result = []

        # keep going while we still have digits or carry left
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0  # current digit of num1
            y = int(num2[j]) if j >= 0 else 0  # current digit of num2


            total = x + y + carry
            result.append(str(total % 10))  # last digit of total
            carry = total // 10  # update carry

            i -= 1
            j -= 1

        return ''.join(reversed(result))  # reverse the result
