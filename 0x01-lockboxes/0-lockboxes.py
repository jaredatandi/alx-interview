#!usr/bin/python3
"""A module to generate keys for lockboxes
"""


def canUnlockAll(boxes):
    """Checks locks for the boxes

    Args:
        boxes (list): an array of boxes

    Returns:
        bool: True or False
    """
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
