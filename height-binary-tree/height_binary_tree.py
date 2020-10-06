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






