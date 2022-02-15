from collections import namedtuple

Interval = namedtuple('Interval', ['low', 'high'])

class ITNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = self.interval.high
        self.left = None
        self.right = None

    def __str__(self):
        return "Low: "+str(self.interval.low)+" High: "+str(self.interval.high)+" Max: "+str(self.max)

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, node, interval):
        if node == None:
            return ITNode(interval)
        
        
        if interval.low < node.interval.low:
            node.left = self.insert(node.left, interval)
        else:
            node.right = self.insert(node.right, interval)

        if interval.high > node.max:
            node.max = interval.high

        return node

    def doOverlap(self, interval1, interval2):
        if interval1.low < interval2.high and interval2.low < interval1.high:
            return True
        return False

    def overlapSearch(self, root, interval):
        if root==None:
            return None

        if self.doOverlap(root.interval, interval):
            return root.interval

        if root.left and root.left.max >= interval.low:
            return self.overlapSearch(root.left, interval)
        
        return self.overlapSearch(root.right, interval)

def printConflicting(appts, n):
    i_tree = IntervalTree()
    i_tree.root = i_tree.insert(None, appts[0])
    for i in range(1, n):
        res = i_tree.overlapSearch(i_tree.root, appts[i])
        if res!=None:
            print("[" , appts[i].low , "," , appts[i].high ,"] Conflicts with [" ,res.low , "," , res.high , "]\n")
        i_tree.root = i_tree.insert(i_tree.root, appts[i])

if __name__ == "__main__":
    appts = []
    appts.append(Interval(1, 5))
    appts.append(Interval(3, 7))
    appts.append(Interval(2, 5))
    appts.append(Interval(10, 15))
    appts.append(Interval(5, 6))
    appts.append(Interval(4, 100))
    n = len(appts)
    print('Following are conflicting intervals:')
    printConflicting(appts, n)