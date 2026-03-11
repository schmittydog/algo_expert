#!/usr/bin/env python3

def minRewards(scores):
    if len(scores) == 1:
        return 1
    if len(scores) == 2:
        return 3
    valleys = set()
    if scores[0] - scores[1] < 0:
        valleys.add(0)
    if scores[len(scores)-1] < scores[len(scores)-2]:
        valleys.add(len(scores)-1)
    for i in range(1, len(scores)-1):
        if scores[i-1] > scores[i] < scores[i+1]:
            valleys.add(i)
    reward_values = [0 for _ in range(len(scores))]
    rewards = 0
    rising = False
    for i in range(len(scores)):
        if i > 0 and (scores[i-1] > scores[i]):
            rising = False
        if i in valleys:
            rising = True
            rewards = 1
        if rising:
            reward_values[i] = rewards
        rewards += 1
    rewards = 0
    rising = False
    for i in range(len(scores)-1,-1):
        if i in valleys:
            rising = True
            rewards = 1
        if rising:
            reward_values[i] = rewards
        rewards += 1

    return sum(reward_values)



print(minRewards([8,4,2,1,3,6,7,9,5]))
