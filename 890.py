from typing import List
class Solution:
    def findAndReplacePattern(self, arr_words: List[str], pattern: str) -> List[str]:
        def encode(word: str) -> List[int]:
            mapping: dict[str, int] = {}
            result: List[int] = []
            next_code: int = 0

            for ch in word:
                if ch not in mapping:
                    mapping[ch] = next_code
                    next_code += 1
                result.append(mapping[ch])

            return result

        pattern_code = encode(pattern)
        final_result = []

        for word in arr_words:
            if encode(word) == pattern_code:
                final_result.append(word)

        return final_result