class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morze = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
            ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
            ".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            transformation=""
            for char in word:
                transformation += morze[ord(char) - 97]
            ans.add(transformation)
        return len(ans)