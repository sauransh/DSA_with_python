import math
'''
given an array of points [[x,y]]
given k -> the number of closest distance coordiantes to be retrieved from points array
formula : eucledian's distance
Note: distance of the points is calculated from the origin

'''

class Solution:
    def KClosest(self, points:list[list[int]], k:int)-> list[list[int]]:
        distances = []
        result =[]

        for x,y in points:
            d = math.sqrt(x**2 + y**2)
            distances.append([d,x,y])
        
        distances.sort(key= lambda x: -x[0])

        while k > 0:
            d, x, y = distances.pop()
            result.append([x,y])
            k-=1

        return result



ss = Solution()

points = [[1,1],[3,3],[3,4],[2,2],[5,6]]
k = 3
print(ss.KClosest(points=points,k=k))
