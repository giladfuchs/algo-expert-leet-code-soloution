# This is an input class. Do not edit.
from collections import defaultdict, deque


class BinaryTree:
    def __init__(self, value, left=None, right=None, **kwargs):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    adj = defaultdict(list)

    def tree_to_graph(node: BinaryTree, parent):
        if not node: return
        if node.left:
            adj[node.value].append(node.left.value)
        if node.right:
            adj[node.value].append(node.right.value)
        if parent:
            adj[node.value].append(parent)
        tree_to_graph(node.left, node.value)
        tree_to_graph(node.right, node.value)

    tree_to_graph(tree, None)
    d_queue = deque([(0, target)])
    seen = set()
    ans = []
    while d_queue:
        d, node = d_queue.popleft()
        if node in seen: continue
        if d > k: break
        if d == k: ans.append(node)

        seen.add(node)
        for _ in adj[node]:
            d_queue.append((d + 1, _))
    print(ans)
    return ans


if __name__ == '__main__':
    tr = BinaryTree(**{"id": "1", "left": BinaryTree(
        **{"id": "2", "left": BinaryTree(**{"id": "4", "left": None, "right": None, "value": 4}),
           "right": BinaryTree(**{"id": "5", "left": None, "right": None, "value": 5}), "value": 2}),
                       "right": BinaryTree(**{"id": "3", "left": None,
                                              "right": BinaryTree(**{"id": "6", "left": BinaryTree(
                                                  **{"id": "7", "left": None, "right": None, "value": 7}),
                                                                     "right": BinaryTree(
                                                                         **{"id": "8", "left": None, "right": None,
                                                                            "value": 8}), "value": 6}),
                                              "value": 3}), "value": 1})

    bb = {"tree": tr,
          "target": 3,
          "k": 2
          }
    findNodesDistanceK(**bb)
