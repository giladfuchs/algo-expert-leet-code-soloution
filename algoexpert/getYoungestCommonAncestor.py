# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    first_way_to_top = []
    while descendantOne:
        first_way_to_top.append(descendantOne.name)
        descendantOne = descendantOne.ancestor
    node_res = None
    while descendantTwo != None:
        if descendantTwo.name in first_way_to_top:
            node_res = descendantTwo
            break
        descendantTwo = descendantTwo.ancestor
    return node_res
