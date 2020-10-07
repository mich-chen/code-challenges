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


def height(root):

    left_height = 0
    right_height = 0

    # if only root node, return 0
    # or if at the end of a branch/leaf
    if root == None:
        return 0

    # increment left height when there is a left node
    if root.left != None:
        left_height = 1 + height(root.left)

    # increment right height when there is a right node
    if root.right != None:
        right_height = 1 + height(root.right)

    # return the larger height between right and left side
    # this accounts for branches with left and right
    return max(left_height, right_height)


if __name__ == '__main__':

    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    tree3 = BinarySearchTree()

    # ***** test 1 ******
    t1 = 5
    arr1 = [3, 1, 7, 5, 4]
    for i in range(t1):
        tree1.create(arr1[i])
    print(height(tree1.root))  # 3

    # ***** test 2 *****
    t2 = 7
    arr2 = [3, 5, 2, 1, 4, 6, 7]
    for i in range(t2):
        tree2.create(arr2[i])
    print(height(tree2.root))  # 3

    # ***** test 3 *****
    t3 = 1
    arr3 = [15]
    for i in range(t3):
        tree3.create(arr3[i])
    print(height(tree3.root))  # 0



