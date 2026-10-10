class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                front = 0
                back = len(row) - 1
                while front <= back:
                    mid = (front + back) // 2
                    if row[mid] < target:
                        front = mid + 1
                    elif row[mid] > target:
                        back = mid - 1
                    else:
                        return True
                return False
        return False
             
