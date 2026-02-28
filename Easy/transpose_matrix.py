#!/usr/bin/env python3

def transposeMatrix(matrix):
    '''
        Time: NxM
        Space: NxM
    '''
    l, w = len(matrix), len(matrix[0])
    trans_matrix = [l*[0] for _ in range(w)]
    for i in range(l):
        for j in range(w):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix
