def layerTraversal(matrix, layer, rows, cols):
    #Right
    for i in range(layer, cols-layer):
        print(matrix[layer][i],end=' ')
        
    #Down
    for i in range(layer+1, rows - layer):
        print(matrix[i][cols-layer-1], end=' ')
    
    #Left
    if cols-layer-1 > layer:
        for i in range(cols-layer-2, layer-1, -1):
            print(matrix[rows-layer-1][i], end=' ')
        
    #Up
    if rows-layer-1 > layer:
        for i in range(rows-layer-2, layer, -1):
            print(matrix[i][layer], end=' ')
    
def spiralTraversalGFG(matrix, rows, cols):
    k = 0
    l = 0
    while k < rows and l < cols:
        for i in range(l, cols):
            print(matrix[k][i], end=' ')
        k += 1
        for i in range(k, rows):
            print(matrix[i][cols-1], end=' ')
        cols -= 1
        if k < rows:
            for i in range(cols-1, (l-1), -1):
                print(matrix[rows-1][i], end=' ')
            rows -= 1
        if l < cols:
            for i in range(rows-1, k-1, -1):
                print(matrix[i][l], end=' ')
            l += 1


def spiralTraversal(matrix, rows, cols):
    for layer in range(min((c+1)//2, (r+1)//2)):
        layerTraversal(matrix, layer, rows, cols)
        print('layer: ', layer)

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        arr = list(range(1, r*c + 1))
        matrix = []
        for i in range(0, r*c, c):
            matrix.append(arr[i:i+c])
        for i in matrix:
            print(i)
        spiralTraversal(matrix, r, c)
        # layerTraversal(matrix, 2, r, c)
        print()