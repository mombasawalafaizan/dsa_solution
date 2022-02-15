from typing import List


def rectangleArea(rectangles: List[List[int]]) -> int:
    x_vals, y_vals = set(), set()
    for x1, y1, x2, y2 in rectangles:
        x_vals.add(x1)
        x_vals.add(x2)
        y_vals.add(y1)
        y_vals.add(y2)

    imapx = sorted(x_vals)
    imapy = sorted(y_vals)
    mapx = {x: i for i, x in enumerate(imapx)}
    mapy = {y: i for i, y in enumerate(imapy)}

    print(mapx, mapy, imapx, imapy)

    grid = [[0] * len(imapy) for _ in imapx]
    for x1, y1, x2, y2 in rectangles:
        for x in range(mapx[x1], mapx[x2]):
            for y in range(mapy[y1], mapy[y2]):
                grid[x][y] = 1

    for i in grid:
        print(i)

    ans = 0
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val:
                ans += (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y])
    return ans % (10**9 + 7)

# Intuition

# Imagine we pass a horizontal line from bottom to top over the shape. We have some active intervals on this horizontal line, which gets updated twice for each rectangle. In total, there are 2 * N2∗N events, and we can update our (up to NN) active horizontal intervals for each update.
# Algorithm

# For a rectangle like rec = [1,0,3,1], the first update is to add [1, 3] to the active set at y = 0, and the second update is to remove [1, 3] at y = 1. Note that adding and removing respects multiplicity - if we also added [0, 2] at y = 0, then removing [1, 3] at y = 1 will still leave us with [0, 2] active.

# This gives us a plan: create these two events for each rectangle, then process all the events in sorted order of y. The issue now is deciding how to process the events add(x1, x2) and remove(x1, x2) such that we are able to query() the total horizontal length of our active intervals.

# We can use the fact that our remove(...) operation will always be on an interval that was previously added. Let's store all the (x1, x2) intervals in sorted order. Then, we can query() in linear time using a technique similar to a classic LeetCode problem, Merge Intervals.


def rectangleArea2(rectangles: List[List[int]]) -> int:
    # Populate events
    OPEN, CLOSE = 0, 1
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((y1, OPEN, x1, x2))
        events.append((y2, CLOSE, x1, x2))
    events.sort()

    def query():
        ans = 0
        cur = -1
        for x1, x2 in active:
            cur = max(cur, x1)
            ans += max(0, x2 - cur)
            cur = max(cur, x2)
        return ans

    active = []
    cur_y = events[0][0]
    ans = 0
    for y, typ, x1, x2 in events:
        # For all vertical ground covered, update answer
        ans += query() * (y - cur_y)

        # Update active intervals
        if typ is OPEN:
            active.append((x1, x2))
            active.sort()  # DO SORTED INSERT INSTEAD
        else:
            active.remove((x1, x2))

        cur_y = y

    return ans % (10**9 + 7)


print(rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
