class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def backtrack(cur_idx1, cur_idx2):
            if (cur_idx1, cur_idx2) in memo:
                return memo[(cur_idx1, cur_idx2)]

            if cur_idx1 == len(s) and cur_idx2 == len(p):
                return True
            if cur_idx2 == len(p):
                return False
            # Handle x* pattern when s is exhausted (skip with zero matches)
            if cur_idx1 == len(s):
                if cur_idx2 < len(p) - 1 and p[cur_idx2 + 1] == '*':
                    return backtrack(cur_idx1, cur_idx2 + 2)
                return False

            if s[cur_idx1] == p[cur_idx2] or p[cur_idx2] == '.':
                # If next is *, can consume one or skip pattern
                if cur_idx2 < len(p) - 1 and p[cur_idx2 + 1] == '*':
                    option1 = backtrack(cur_idx1 + 1, cur_idx2)
                    option2 = backtrack(cur_idx1, cur_idx2 + 2)
                    option3 = backtrack(cur_idx1 + 1, cur_idx2 + 2)
                    memo[(cur_idx1, cur_idx2)] = option1 or option2 or option3
                    return memo[(cur_idx1, cur_idx2)]
                memo[(cur_idx1, cur_idx2)] = backtrack(cur_idx1 + 1, cur_idx2 + 1)
                return memo[(cur_idx1, cur_idx2)]
            else:
                # No match — only valid move is skipping a x* pattern
                if cur_idx2 < len(p) - 1 and p[cur_idx2 + 1] == '*':
                    memo[(cur_idx1, cur_idx2)] =  backtrack(cur_idx1, cur_idx2 + 2)
                    return memo[(cur_idx1, cur_idx2)]
                memo[(cur_idx1, cur_idx2)] = False
                return False

        memo = {}
        return backtrack(0, 0)