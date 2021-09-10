from collections import deque 
import heapq
def solution(jobs):
    jobs.sort()
    jobs = deque(jobs)
    
    answer, total_job = 0, len(jobs)
    start, now = -1, 0
    tasks = []
    while jobs or tasks:
        while jobs and start < jobs[0][0] <= now:
            requested_time, job = jobs.popleft()
            heapq.heappush(tasks, (job, requested_time))
        if tasks:
            current_job, requested_time = heapq.heappop(tasks)
            start = now
            now += current_job
            answer += (now-requested_time)
        else:
            now += 1
    
    return answer//total_job
