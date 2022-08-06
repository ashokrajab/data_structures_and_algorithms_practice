"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

 

Constraints:

    1 <= task.length <= 104
    tasks[i] is upper-case English letter.
    The integer n is in the range [0, 100].
"""
from typing import List
from collections import deque
from heapq import heapify,heappop,heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = {}
        task_q = deque()
        
        for task in tasks:
            task_count[task] = 1 + task_count.get(task, 0)
            
        task_heap = [(-count,task) for task,count in task_count.items()]
        heapify(task_heap)
        
        output = 0
        time = 0
        while task_heap or task_q:
            time += 1
            output += 1
            if task_q and task_q[0][0]==time:
                time,task,count = task_q.popleft()
                heappush(task_heap,(count*-1,task))
            
            if task_heap:
                count, task = heappop(task_heap)
                count *= -1
                if count >1:
                    task_q.append((time+n+1,task,count-1))
        return output