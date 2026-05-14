class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        ans = []
        for num in nums:
            if num not in my_map:
                my_map[num] = 1
            else:
                my_map[num] += 1

        my_map2 = {}
        for num in my_map:
            if my_map[num] in my_map2:
                my_map2[my_map[num]].append(num)
            else:
                my_map2[my_map[num]] = [num]
        counts = []
        for num in my_map2:
            counts.append(num)
        
        counts.sort(reverse = True)
        total = 0
        ans = []
        for count in counts:
            num_of_entries = my_map2[count]
            for i in range(0,len(num_of_entries)):
                total = total + 1
                ans.append(num_of_entries[i])
                if total >=k:
                    return ans