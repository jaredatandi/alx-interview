#!usr/bin/python3
"""A module to generate keys for lockboxes
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        visited.add(box)

        keys = boxes[box]
        for key in keys:
            if key not in visited:
                stack.append(key)

    return len(visited) == n
