import sys
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinTree:
    idx = 0
    child_list = []

    def __init__(self, child_list) -> None:
        self.child_list = child_list
        self.root = self.make_tree(-float('inf'), float('inf'))

    def make_tree(self, left, right):
        if self.idx >= len(self.child_list):
            return None

        value = self.child_list[self.idx]
        
        # 추가된 부분: 범위에 맞지 않는 경우 None을 반환
        if not left < value < right:
            return None

        self.idx += 1
        node = Node(value)
        node.left = self.make_tree(left, value)
        node.right = self.make_tree(value, right)
        return node

child_list = []
while True:
    try:
        child_list.append(int(input()))
    except EOFError:  # 입력이 끝날 때까지 받기 위해 EOFError 사용
        break

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

tree = BinTree(child_list)
postorder(tree.root)