class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    """Return lowest common ancestor of v1 and v2.

    Classical Binary Search Tree problem."""

    if root == None:
        return 0

    # lca must fall between v1 and v2

    # if current node is larger than both values
    # then recursively traverse to left
    # print('print', root.info)
    if root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)

    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)

    # if current node falls between the two values
    # then it is least common ancestor
    # reduced all possible answers by binary search O(log n)
    return root


"""
# Alternative Solution: no recursion, BST

def lca(root, v1, v2):

    current = root

    while current.info:

        if current.info > v1 and current.info > v2:
            current = current.left

        elif current.info < v1 and current.info < v2:
            current = current.right

        else:
            return current

    return current
"""




if __name__ == '__main__':
    
    # ***** test 1 *****
    tree1 = BinarySearchTree()
    arr1 = [4, 2, 3, 1, 7, 6]
    for i in range(len(arr1)):
        tree1.create(arr1[i])
    v1 = [1, 7]
    ans1 = lca(tree1.root, v1[0], v1[1])
    print (ans1.info)  # 4

    # ***** Test 2 *****
    tree2 = BinarySearchTree()
    arr2 = [8, 4, 9, 1, 2, 3, 6, 5]
    for i in range(len(arr2)):
        tree2.create(arr2[i])
    v2 = [1, 2]
    ans2 = lca(tree2.root, v2[0], v2[1])
    print(ans2.info)  # 1