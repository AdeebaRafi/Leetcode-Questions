class Solution(object):
    def generate(self, numRows):
        result = []  # final answer

        for i in range(numRows):
            row = [1] * (i + 1)  # sab values 1 se bhari hoti hain

            for j in range(1, i):  # beech ke elements update karne hain
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)  # row ko triangle mein daal do

        return result  # final triangle