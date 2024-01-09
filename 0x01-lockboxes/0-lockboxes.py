#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    '''canUnlockAll function to check if all boxes can be opened'''
    number_of_boxes = len(boxes)
    checked_boxes = [0]
    unchecked_boxes = set(boxes[0]).difference(set([0]))

    while len(unchecked_boxes) > 0:
        boxNumber = unchecked_boxes.pop()
        if not boxNumber or boxNumber >= number_of_boxes or boxNumber < 0:
            continue
        if boxNumber not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[boxNumber])
            checked_boxes.append(boxNumber)
    return number_of_boxes == len(checked_boxes)
