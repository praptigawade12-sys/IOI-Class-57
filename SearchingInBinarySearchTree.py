class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root,key):
    if root is None:
        return Node(key)

    else:
        if root.data == key:
            return root
        elif root.data > key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

def search(root,key):
    if root is None or root.data == key:
        return root

    if root.data > key:
        return search(root.left,key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end = " ")
        inorder(root.right)

root = Node(50)
root = insert(root,30)
root = insert(root,20)
root = insert(root,40)
root = insert(root,70)
root = insert(root,60)
root = insert(root,80)

print("Binnary tree - Inorder Traverval : ")
inorder(root)
print()

k = int(input("Enter the element to search :"))

if search(root,k):
    print("Element FOUND")
else:
    print("Element NOT FOUND")