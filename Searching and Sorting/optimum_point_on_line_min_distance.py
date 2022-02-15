from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['a', 'b', 'c'])

def compute(p, n, l, X):
    summation = 0
    dist = lambda x, y, p: ((x-p.x)**2 + (y-p.y)**2)**0.5
    Y = -1 * (l.c + l.a * X)/l.b
    for i in range(n):
        summation += dist(X, Y, p[i])
    return summation

def findOptimumCost(p, n, l):
    low = -1e6
    high = 1e6
    endpoint = 0.05
    while (high - low) > endpoint:
        mid1 = low + (high - low)/3
        mid2 = high - (high - low)/3
        dist1 = compute(p, n, l, mid1)
        dist2 = compute(p, n, l, mid2)
        if dist1 < dist2:
            high = mid2
        else:
            low = mid1
    return (low+high)/2

if __name__ == "__main__":
    l = Line(1, -1, -3)
    N = 5
    points = [Point(-3, -2), Point(-1, -0), Point(-1, 2), Point(1, 2), Point(3, 4)]
    x = findOptimumCost(points, N, l)
    print('Optimum point: X = {:.2f}, Y = {:.2f}'.format(x, -1 * (l.c + l.a * x)/l.b))
    print('Summation distance from all points: {:.2f}'.format(compute(points, N, l, x)))