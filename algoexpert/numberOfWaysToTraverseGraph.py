import math
def numberOfWaysToTraverseGraph(width, height):
    return math.comb(width+height-2, width-1)

if __name__ == '__main__':
    print(numberOfWaysToTraverseGraph(2, 3))
