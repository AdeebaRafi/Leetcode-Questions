class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        bucket = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                bucket[int(s)] += 1
                bucket[int(g)] -= 1

        # Count the number of cows
        total_matches = len(secret) - bulls
        unmatched_digits = sum(x for x in bucket if x > 0)
        cows = total_matches - unmatched_digits

        return f"{bulls}A{cows}B"