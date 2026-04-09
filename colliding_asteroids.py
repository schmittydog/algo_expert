#!/usr/bin/env python3

def collidingAsteroids(asteroids):
    stack = []
    asteroids = [asteroids[i] for i in range(len(asteroids)-1, -1, -1)]
    while asteroids:
        a = asteroids.pop()
        if a > 0:
            stack.append(a)
        else:
            if not stack or stack[-1] < 0:
                stack.append(a)
            else:
                if -a > stack[-1]:
                    stack.pop()
                    asteroids.append(a)
                elif -a == stack[-1]:
                    stack.pop()
    return stack
