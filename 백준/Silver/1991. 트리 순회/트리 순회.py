N = int(input())

def preorder(node):
    if node :
        print(node.name, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node :
        inorder(node.left)
        print(node.name, end='')
        inorder(node.right)

def postorder(node):
    if node :
        postorder(node.left)
        postorder(node.right)
        print(node.name, end='')

    # 루트 
    # 왼쪽자식
    # 오른쪽 자식


class Node:

    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None
    

class BinaryTree:

    node_list = {}
    
    # 루트를 구현하는 것 까지는 이해했는데, 여기서 루트를 아래로 쭉쭉 이어 만드는 방법에 대해서는?
    def __init__(self, node_list) -> None:
        self.root = Node('A')
        self.node_list = node_list
        self.make_node(self.root, 'A')
        
        # A, [B,C]
    def make_node(self, parent, key):
        left, right = self.node_list[key]

        if left != '.':
            parent.left = Node(left)
            self.make_node( parent.left , left)
        
        if right != '.':
            parent.right = Node(right)
            self.make_node( parent.right, right)



# A가 항상 부모노드

# bin_tree = BinaryTree()

root_dict = {}

for i in range(N):
    root, a,b = input().split()
    root_dict[root] = [a,b]

bin_tree = BinaryTree(root_dict)
preorder(bin_tree.root)
print()
inorder(bin_tree.root)
print()
postorder(bin_tree.root)