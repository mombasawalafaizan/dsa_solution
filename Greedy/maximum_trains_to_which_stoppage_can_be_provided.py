class TrainInfo:
    def __init__(self, arrival, departure):
        self.arvl = arrival
        self.dptr = departure

def maxStop(arr, n, p):
    pltfrms = [[] for _ in range(p)]
    
    for i in range(n):
        pltfrms[arr[i][2]-1].append(TrainInfo(arr[i][0], arr[i][1]))
    
    for i in range(p):
        pltfrms[i].sort(key=lambda x: x.dptr)
    
    stoppedTrains = 0

    for i in range(p):
        if len(pltfrms[i]) != 0:
            stoppedTrains += 1
            idx = 0
            for j in range(1, len(pltfrms[i])):
                if pltfrms[i][j].arvl >= pltfrms[i][idx].dptr:
                    stoppedTrains += 1
                    idx = j
    
    return stoppedTrains



if __name__ == '__main__':
    platforms = 3
    trains = [[1000, 1030, 1],[1010, 1020, 2], [1030, 1230, 2], [1010, 1030, 1],  [1200, 1230, 3], [900, 1005, 1] ]
    no_of_trains = len(trains)
    data = []
    print(maxStop(trains, no_of_trains, platforms))