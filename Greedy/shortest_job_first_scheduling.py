class Job:
    def __init__(self, process_id, arrival, burst):
        self.id = process_id
        self.arrival = arrival
        self.burst = burst
        self.completion = 0
        self.tat = 0
        self.waiting = 0

    def __lt__(self, other):
        if self.arrival == other.arrival:
            return self.burst < other.burst
        return self.arrival < other.arrival

def completionTime(jobs):
    n = len(jobs)

    min_idx = 0
    for i in range(1, n):
        if jobs[i] < jobs[min_idx]:
            min_idx = i
    jobs[0], jobs[min_idx] = jobs[min_idx], jobs[0]
            
    for i in range(n):
        latest_time = jobs[i-1].completion if i != 0 else jobs[0].arrival
        min_burst = jobs[i].burst
        val = i

        # Find the lowest burst time from [i, n)
        if i!=0:
            for j in range(i+1, n):
                # If the job has arrived and has lower burst time than the previous 
                # processed jobs
                # NOTE: For comparing min_burst >= is taken because, we have to take the latest
                # job first
                if jobs[j].arrival <= latest_time and min_burst >=  jobs[j].burst:
                    # If same min_burst, then choose the one with less arrival time
                    if min_burst == jobs[j].burst and jobs[val].arrival < jobs[j].arrival:
                        continue
                    val = j
                    min_burst = jobs[j].burst


        # Compute the information for current shortest job
        jobs[val].completion = latest_time + jobs[val].burst
        jobs[val].tat = jobs[val].completion - jobs[val].arrival
        jobs[val].waiting = jobs[val].tat - jobs[val].burst
        
        # Swap the shortest job with current job which may not have
        # been processed
        jobs[i], jobs[val] = jobs[val], jobs[i]
        

if __name__ == '__main__':
    jobs = []
    jobs.append(Job(5, 9, 8))
    jobs.append(Job(1, 1, 7))
    jobs.append(Job(3, 6, 2))
    jobs.append(Job(2, 3, 3))
    jobs.append(Job(4, 7, 10))
    completionTime(jobs)
    print("Final Result...") 
    print("Process ID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(len(jobs)): 
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(
            jobs[i].id,
            jobs[i].arrival,
            jobs[i].burst,
            jobs[i].completion,
            jobs[i].tat,
            jobs[i].waiting,
        ))

