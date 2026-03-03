def diceThrows(numDice, numSides, target):
    cache = [1] + target * [0]
    for num in range(1, numDice+1):
        for side in range(1, numSides+1):
            for i in range(target-side, -1, -1):
                cache[i+side] += cache[i]
    print(cache)
    return cache[-1]




