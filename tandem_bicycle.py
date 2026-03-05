#!/usr/bin/env python3

def tandemBicycle(reds, blues, fastest):
    '''
        Time: NLogN
        Space: N
    '''
    if fastest:
        reds.sort(reverse=True)
    else:
        reds.sort()
    blues.sort()
    speed_sum = 0
    for i in range(len(reds)):
        speed_sum += max(reds[i], blues[i])
    return speed_sum
