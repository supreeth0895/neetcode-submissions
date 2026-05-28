#SUPREETH
# Use two pointers (start, end) to maintain a sliding window over s.
# Expand end when window doesn't satisfy t, shrink start when it does.
# Track best window seen so far when all chars of t are covered.

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def compare_two_maps():
            # Returns total count of chars in t not yet satisfied by current window
            diff = 0
            for key in my_map2:
                if key not in my_map1:
                    diff = diff+my_map2[key]
                else:
                    if my_map1[key] < my_map2[key]:
                        diff = diff+ my_map2[key] - my_map1[key]
            return diff

        
        min_length_of_substring = 1000000
        min_substring_start = 0
        min_substring_end = 0

        if len(s) < len(t):
            return ""

        # Build frequency map for t
        my_map2 = {}
        for ch in t:
            if ch not in my_map2:
                my_map2[ch] = 1
            else:
                my_map2[ch] = my_map2[ch] + 1

        my_map1 = {}

        # Move start to first char that exists in t
        start = 0
        while True:
            if s[start] not in my_map2:
                start = start+1
                if start > len(s)-1:
                    return ""
            else:
                break

        # Initialize window [start, start+len(t)) into my_map1
        end = start + len(t)

        for i in range(start, end):
            ch = s[i]
            if ch not in my_map1:
                my_map1[ch] = 1
            else:
                my_map1[ch] = my_map1[ch] + 1

        # end <= len(s) allows end to equal len(s) so the last valid window is not missed
        while start <= end and end <= len(s):
            
            diff = compare_two_maps()

            if diff > 0:
                # Window does not satisfy t yet — expand right
                # Guard end == len(s) to avoid index out of bounds on s[end]
                if end == len(s):
                    break
                if s[end] not in my_map1:
                    my_map1[s[end]] = 1
                else:
                    my_map1[s[end]] = my_map1[s[end]] +1
                end = end+1

            elif diff == 0:
                # Window satisfies t — record if smallest so far, then shrink left
                if min_length_of_substring > (end-start):
                    min_substring_start = start
                    min_substring_end = end
                    min_length_of_substring  = end-start

                my_map1[s[start]] = my_map1[s[start]] - 1
                if my_map1[s[start]] == 0:
                    my_map1.pop(s[start])
                start = start+1
            
        return s[min_substring_start:min_substring_end]