import math
import sys


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def max_points_on_a_line_containing_point_i(i):
            """
            Compute the max number of points
            for a line containing point i.
            """
            def slope_coprime(x1, y1, x2, y2):
                """ to avoid the precision issue with the float/double number,
                    using a pair of co-prime numbers to represent the slope.
                """
                delta_x, delta_y = x1 - x2, y1 - y2
                if delta_x == 0:    # vertical line
                    return (0, 0)
                elif delta_y == 0:  # horizontal line
                    return (sys.maxsize, sys.maxsize)
                elif delta_x < 0:
                    # to have a consistent representation,
                    #   keep the delta_x always positive.
                    delta_x, delta_y = - delta_x, - delta_y
                gcd = math.gcd(delta_x, delta_y)
                slope = (delta_x / gcd, delta_y / gcd)
                return slope

            def add_line(i, j, count):
                """
                Add a line passing through i and j points.
                Update max number of points on a line containing point i.
                Update a number of duplicates of i point.
                """
                # rewrite points as coordinates
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                # add a horisontal line : y = const
                if y1 == y2:
                    nonlocal horizontal_lines
                    horizontal_lines += 1
                    count = max(horizontal_lines, count)
                # add a line : x = slope * y + c
                # only slope is needed for a hash-map
                # since we always start from the same point
                else:
                    slope = slope_coprime(x1, y1, x2, y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    print(i, j, slope, lines[slope])
                    count = max(lines[slope], count)
                return count

            # init lines passing through point i
            lines, horizontal_lines = {}, 1
            # One starts with just one point on a line : point i.
            count = 1
            # Compute lines passing through point i (fixed)
            # and point j (interation).
            # Update in a loop the number of points on a line
            # and the number of duplicates of point i.
            for j in range(i + 1, n):
                count = add_line(i, j, count)
            return count

        # If the number of points is less than 3
        # they are all on the same line.
        n = len(points)
        if n < 3:
            return n

        max_count = 1
        # Compute in a loop a max number of points
        # on a line containing point i.
        for i in range(n - 1):
            max_count = max(
                max_points_on_a_line_containing_point_i(i), max_count)
        return max_count


if __name__ == '__main__':
    print('hi')
    x = 0
    print('hello') if x == 1 else print('hi')
    # s = 'emere angene' /
    #         "me"
    print('mere angne'
          " me")