class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        my_map = {}
        max_len = 0

        while right < len(s):
            if s[right] not in my_map:
                my_map[s[right]] = 1
                right = right + 1
            else:
                my_map[s[right]] = my_map[s[right]] +1
                right = right + 1

            max_val = 0
            max_char = 'A'
            total_count_in_substring = 0
            
            for key in my_map:
                if my_map[key] > max_val:
                    max_val = my_map[key] 
                    max_char = key
                total_count_in_substring =total_count_in_substring + my_map[key]
            total_letters_that_can_be_replaced = total_count_in_substring - max_val

            if total_letters_that_can_be_replaced > k :
                while total_letters_that_can_be_replaced > k:
                    my_map[s[left]] = my_map[s[left]] - 1
                    if my_map[s[left]] == 0:
                        my_map.pop(s[left])
                    left = left + 1
                    
                    max_val = 0
                    total_count_in_substring = 0
                    for key in my_map:
                        if my_map[key] > max_val: max_val = my_map[key]
                        total_count_in_substring += my_map[key]
                    total_letters_that_can_be_replaced = total_count_in_substring - max_val
            
            max_len = max(max_len, right - left)

        return max_len