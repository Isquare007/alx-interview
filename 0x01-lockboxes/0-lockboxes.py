#!/usr/bin/python3
"""``Lockboxes`` module"""


def canUnlockAll(boxes):
    """
        Return True if all boxes can be opened, else return False
            Args:
                boxes (list of list): A list
    """
    n = len(boxes)
    boxes_state = [False] * n
    boxes_state[0] = True

    box_stack = [0]

    while box_stack:
        curr_box = box_stack.pop()
        for key in boxes[curr_box]:
            if key >= 0 and key < n and not boxes_state[key]:
                boxes_state[key] = True
                box_stack.append(key)

    return all(boxes_state)
