#!/usr/bin/env python3

from queue import deque
def staircaseTraversal(height, steps):
    '''
        Time: height
        Space: steps
        Track with queue
    '''
    count = 1
    q = deque((steps-1)*[0] + [1])
    for n in range(1, height+1):
        q.append(count)
        count *= 2
        count -= q.popleft()
    return q[-1]


def staircaseTraversal(height, maxSteps):
    '''
        Time: height * maxSteps
        Space: maxSteps
        Dynamic Programming
    '''
    dp = [1] + height * [0]
    for i in range(len(dp)):
        for j in range(1, maxSteps+1):
            if i + j >= len(dp):
                break
            dp[i+j] += dp[i]
    return dp[-1]
