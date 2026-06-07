class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0,1]
        cur_max = 1
        while cur_max < n:
            cur_max = cur_max*2
            cur_ans_len = len(answer)
            for i in range(0, cur_ans_len):
                answer.append(answer[i]+1)
        return answer[:n+1]
                

# 0
# 1
# 01
# 10
# 100
# 101
# 110
# 111
        