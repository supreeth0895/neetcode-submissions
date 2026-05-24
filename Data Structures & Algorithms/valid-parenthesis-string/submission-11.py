class Solution:
    def checkValidString(self, s: str) -> bool:
        #Calauclate the maximum number of open brackets, and minimumn number of open brackets we can be left with.
        # If both are 0, then return 0.
        # if one is positive and one is negetive, retruen True.
        # If both are positive or Both are negetive, returm False
        # And then, at any point, if the number of open brackets is negetive, then return False

        # 3 edge cases:
        # At any point, if there are More closing brackets than open brackets ie, both minleft and maxleft will be negetive. Check this every iteration and return false if this is true.
        # At anypoint, when we see a *, a * can be closing bracket ONLY if there is opening bracket in excess, meaning, only if bracket_open_count_min > 0. Otherwise, * MUST be (.
        # At the end idx, if there are More open brackets than close brackets ie, both minleft and maxleft will be positive, then, we can check this at the end, and return False

        bracket_open_count_min = 0
        bracket_open_count_max = 0
        for ch in s:
            if ch == '(':
                bracket_open_count_min =bracket_open_count_min + 1
                bracket_open_count_max = bracket_open_count_max + 1
            elif ch == ')':
                bracket_open_count_min = bracket_open_count_min - 1
                bracket_open_count_max = bracket_open_count_max - 1
            elif ch == '*':
                bracket_open_count_min = bracket_open_count_min - 1
                bracket_open_count_max = bracket_open_count_max + 1
            if bracket_open_count_max < 0:
                return False
            if bracket_open_count_min < 0 and bracket_open_count_max >= 0 :
                #This means, we have considered some stars could be closing brackets earlier possibly, but at this point, having that * as a closing bracket is no longer possible.
                #Let's update bracket_open_count_min to reflect this:
                bracket_open_count_min = 0


        if bracket_open_count_min > 0 and bracket_open_count_max >= 0 :
            return False
        return True









        