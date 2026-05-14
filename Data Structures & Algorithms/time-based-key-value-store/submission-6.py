class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_map:
            self.my_map[key] = [tuple([timestamp, value])]
        else:
            self.my_map[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_map:
            return ""
        list_of_values = self.my_map[key]

        if timestamp < list_of_values[0][0]:
            return ""
        start = 0
        end = len(list_of_values)-1

        while start <= end:
            mid = math.trunc((start+end)/2)
            if timestamp == list_of_values[mid][0]:
                return list_of_values[mid][1]
            if timestamp > list_of_values[mid][0] :
                start = mid +1
            else:
                end = mid-1
        return list_of_values[end][1]


        
# 10 20 30

# 1 3
# 3