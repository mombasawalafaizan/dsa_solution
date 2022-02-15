from queue import Queue

def printStream(chars, n):
    letters = [0] * 26
    q = Queue()
    for i in range(n):
        if letters[ord(chars[i])-97]==0:
            q.put(chars[i])
        letters[ord(chars[i])-97]+=1
        while not q.empty() and letters[ord(q.queue[0])-97]>1:
            q.get() 
        if q.empty():
            print('-1', end=' ')
        else:
            print(q.queue[0], end=' ')
    print()
        
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        chars = input().split()
        printStream(chars, n)