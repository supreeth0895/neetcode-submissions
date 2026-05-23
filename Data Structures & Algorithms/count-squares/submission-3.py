class CountSquares:

    def __init__(self):
        self.my_map = {}
        self.max_row, self.max_col = 0,0
        self.min_row, self.min_col = 1000, 1000

    def add(self, point: List[int]) -> None:
        if point[0] > self.max_row:
            self.max_row = point[0]
        if point[1] > self.max_col:
            self.max_col = point[1]
        if point[0] < self.min_row:
            self.min_row = point[0]
        if point[1] < self.min_col:
            self.min_col = point[1]

        point_tuple = tuple(point)
        if point_tuple in self.my_map:
            self.my_map[point_tuple] = self.my_map[point_tuple] + 1
        else:
            self.my_map[point_tuple] = 1
    
        

    def count(self, point: List[int]) -> int:
        total_prod  = 0
        cur_point_val = 1
        point_tuple = tuple(point)
        if point_tuple in self.my_map:
            cur_point_val = self.my_map[point_tuple]

        for i in range(self.min_row,self.max_row+1):
            for j in range(self.min_col,self.max_col+1):
                if (i,j) == point_tuple:
                    continue
                if abs(point[0]-i) == abs(point[1]-j) and (point[0],j) in self.my_map and (i,point[1]) in self.my_map and (i, j) in self.my_map:
                    prod = self.my_map[(i,j)]*self.my_map[(point[0],j)]*self.my_map[(i,point[1])]*cur_point_val
                    total_prod = total_prod + prod
        return total_prod
        


        
