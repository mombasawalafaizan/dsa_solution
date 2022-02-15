class Job:
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


def find(s, parent):
    '''This function helps to find the root of the disjoint set'''
    if s == parent[s]:
        return s
    parent[s] = find(parent[s], parent)
    return parent[s] 

# This is a O(nlogn) solution using disjoint sets
def JobScheduling(Jobs,n):
    '''
    :param Jobs: list of "Job" class defined in driver code, with "profit" and "deadline".
    :param n: total number of jobs
    :return: A list of size 2 having list[0] = count of jobs and list[1] = max profit
    '''
    Jobs.sort(key = lambda x: x.profit, reverse=True) # Sort jobs wrt profit
    maxprofit = 0
    jobs_done = 0
    max_deadline = max(Jobs, key = lambda x: x.deadline) # Get the max deadline
    parent = [i for i in range(max_deadline.deadline+1)]
    for i in range(n):
        available_slot = find(Jobs[i].deadline, parent)
        # If root is 0, no slot available else
        # the current job can be placed in the available slot and find the parent of 
        # available_slot using by calculating the parent of the previous slot
        if available_slot > 0:
            maxprofit += Jobs[i].profit
            jobs_done += 1
            parent[available_slot] = find(available_slot-1, parent)
    return [jobs_done, maxprofit]

    # # This is a simple solution but uses O(n^2) time complexity
    # occupied = [False] * (n+1)
    # for i in range(n):
    #     cur_job = Jobs[i]
    #     j = min(cur_job.deadline, n)
    #     while occupied[j]:
    #         j-=1
    #     if j > 0:
    #         occupied[j] = True
    #         maxprofit += cur_job.profit
    #         jobs_done += 1
    # return [jobs_done, maxprofit]