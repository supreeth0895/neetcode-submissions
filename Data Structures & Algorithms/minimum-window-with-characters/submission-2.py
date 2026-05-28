class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare_two_maps():
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

        my_map2 = {}
        for ch in t:
            if ch not in my_map2:
                my_map2[ch] = 1
            else:
                my_map2[ch] = my_map2[ch] + 1

        my_map1 = {}

        start = 0
        while True:
            if s[start] not in my_map2:
                start = start+1
                if start > len(s)-1:
                    return ""
            else:
                break

        end = start + len(t)

        for i in range(start, end):
            ch = s[i]
            if ch not in my_map1:
                my_map1[ch] = 1
            else:
                my_map1[ch] = my_map1[ch] + 1

        while start <= end and end <= len(s):
            

            diff = compare_two_maps()
            # print(start, end, diff, my_map2, my_map1)
            if diff > 0:
                if end == len(s):
                    break
                if s[end] not in my_map1:
                    my_map1[s[end]] = 1
                else:
                    my_map1[s[end]] = my_map1[s[end]] +1
                end = end+1
            elif diff == 0 :
                # print(end-start, min_length_of_substring)
                if min_length_of_substring > (end-start):
                    min_substring_start = start
                    min_substring_end = end
                    min_length_of_substring  = end-start
                    # print("Hi", end, start, min_length_of_substring)

                my_map1[s[start]] = my_map1[s[start]] - 1
                if my_map1[s[start]] == 0:
                    my_map1.pop(s[start])
                start = start+1
            
        return s[min_substring_start:min_substring_end]