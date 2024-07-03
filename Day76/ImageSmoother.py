import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0 for x in range(len(img[0]))] for y in range(len(img))]
        for row in range(len(img)):
            for col in range(len(img[0])):
                total = 1
                s = img[row][col]
                a,b = row-1, col
                if a>=0:
                    total+=1
                    s+=img[a][b]
                a,b=row+1,col
                if a<len(img):
                    total+=1
                    s+=img[a][b]
                a,b = row, col-1
                if b>=0:
                    total+=1
                    s+=img[a][b]
                a,b = row, col+1
                if b<len(img[0]):
                    total+=1
                    s+=img[a][b]
                a,b = row-1, col-1
                if a>=0 and b>=0:
                    total+=1
                    s+=img[a][b]
                a,b = row-1, col+1
                if a>=0 and b<len(img[0]):
                    total+=1
                    s+=img[a][b]
                a,b = row+1, col-1
                if a<len(img) and b>=0:
                    total+=1
                    s+=img[a][b]
                a,b = row+1, col+1
                if a<len(img) and b<len(img[0]):
                    total+=1
                    s+=img[a][b]
                
                avg = math.floor(s/total)
                res[row][col]=avg
        return res