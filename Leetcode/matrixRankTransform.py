# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3874/

# The basic algorithm to solve the above stated problem is to sort the matrix and then, one-by-one pick the elements.
# We maintain a rows and columns array to store the max-rank found in that row and column and rank the element with
# max(row[i], col[j]) + 1 rank.

# The main problem arises when duplicates are found, because from the condition in the problem if p==q in row or column:
# rank(p) == rank(q). So, we have find the duplicate with the maximum rank from a group of duplicates and rank all the duplicates
# with it.
# To encounter this we use union-find algorithm
# The idea is to group elements with same values and belonging to a cluster of same rows and columns
# into disjoint sets.
# eg. [[1, 2,  3,   3],
#      [3, 10, 4, 18],
#      [7, 3,  6,  5],
#      [8, 3,  9,  3]]
# Here, 3 is occurring more than 1 time. So, we have to group it.
# For that, all the 3s except 3 at position (1, 0) will be in a group and 3 at position (1, 0)
# in the other group(disjoint-set).
# For a set, we have to maintain this property, the root of the set will contain the maximum rank
# of an element in that group. All children points to root directly(path-compression is used).
# NOTE: The main reason we are using disjoint set is because of the above stated condition.

# Then, after we have separated elements into disjoint sets, make the rank of all the elements as the
# maximum rank found in that group.
from collections import defaultdict


def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


def union(subsets, u, v):
    subsets[v].parent = u
    subsets[u].rank = max(subsets[u].rank, subsets[v].rank)


class Subsets:
    def __init__(self, parent, rank) -> None:
        self.parent = parent
        self.rank = rank


def matrixRankTransform(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    r = len(matrix)
    c = len(matrix[0])
    arr = []
    k = 0
    for i in range(r):
        for j in range(c):
            arr.append([k, matrix[i][j]])
            k += 1

    max_r_row = [0 for _ in range(r)]
    max_r_col = [0 for _ in range(c)]
    arr.sort(key=lambda x: x[1])

    res = [[0 for _ in range(c)] for _ in range(r)]

    i = 0
    while i < (r*c):
        el = arr[i][1]
        cur_r = arr[i][0] // c
        cur_c = arr[i][0] % c
        subsets = dict()
        rows = defaultdict(list)
        cols = defaultdict(list)
        j = i
        while j < (r*c-1) and el == arr[j+1][1]:

            subsets[arr[j][0]] = Subsets(arr[j][0], max(
                max_r_row[arr[j][0] // c], max_r_col[arr[j][0] % c]))
            rows[arr[j][0] // c].append(arr[j][0])
            cols[arr[j][0] % c].append(arr[j][0])
            j += 1

        # Duplicates found, do union-find algorithm
        if j != i:
            subsets[arr[j][0]] = Subsets(arr[j][0], max(
                max_r_row[arr[j][0] // c], max_r_col[arr[j][0] % c]))
            rows[arr[j][0] // c].append(arr[j][0])
            cols[arr[j][0] % c].append(arr[j][0])
            j += 1

            # Do union-find
            for k in range(i, j):
                u_rep = find(subsets, arr[k][0])
                for edges in (rows[arr[k][0]//c], cols[arr[k][0] % c]):
                    for v in edges:
                        v_rep = find(subsets, v)
                        if u_rep != v_rep:
                            union(subsets, u_rep, v_rep)

                    # Optimization
                    if edges == rows[arr[k][0]//c]:
                        rows[arr[k][0]//c] = [u_rep]
                    else:
                        cols[arr[k][0] % c] = [u_rep]
            for u in subsets:
                root = find(subsets, u)
                max_r_row[u // c] = subsets[root].rank + 1
                max_r_col[u % c] = subsets[root].rank + 1
                res[u//c][u % c] = subsets[root].rank + 1
            i = j - 1
        else:
            temp = max(max_r_row[cur_r], max_r_col[cur_c])
            res[cur_r][cur_c] = temp + 1
            max_r_row[cur_r] = temp + 1
            max_r_col[cur_c] = temp + 1
        i += 1
    return res


if __name__ == '__main__':
    mat = [[1, 2, 3, 3],
           [3, 10, 4, 18],
           [7, 3, 6, 5],
           [8, 3, 9, 3]]
    print(matrixRankTransform(mat))
