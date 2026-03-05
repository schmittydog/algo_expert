#!/usr/bin/env python3

def classPhotos(reds, blues):
    '''
        Time: NLogN
        Space: N
        GREEDY
    '''
    front = sorted(reds)
    back = sorted(blues)
    if front[0] > back[0]:
        front, back = back, front
    for i in range(len(front)):
        if not back[i] > front[i]:
            return False
    return True
