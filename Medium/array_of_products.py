#!/usr/bin/env python3

def arrayOfProducts(array):
    '''
        Time: N
        Space: N
    '''
    products = len(array) * [1]
    prev_prod = 1
    for i in range(len(array)):
        products[i] *= prev_prod
        prev_prod *= array[i]
    prev_prod = 1
    for i in range(len(array)-1, -1, -1):
        products[i] *= prev_prod
        prev_prod *= array[i]
    return products
