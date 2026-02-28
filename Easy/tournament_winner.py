#!/usr/bin/env python3
def tournamentWinner(competitions, results):
    '''
        Time: N
        Space: N
    '''
    scores = {}
    for i in range(len(results)):
        if results[i] == 1:
            scores[competitions[i][0]] = scores.get(competitions[i][0], 0) + 3
        else:
            scores[competitions[i][1]] = scores.get(competitions[i][1], 0) + 3
    winner = None
    max_score = 0
    for k, v in scores.items():
        if v > max_score:
            max_score = v
            winner = k
    return winner
