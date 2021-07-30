"""
Author: Mageza Shalom
Cohort: 2
Retake Assessment: 3
Part III : Array Based Binary Search Tree
"""


# Here I start by creating our Binary Search Tree Node
class BinarySearchTreeNode:
    # Then for this created class I initialize the attributes
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        
	# Here, I define the function to insert new data
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

 	# Then Here the function To deleted the data
    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
        
# Then here I find data and return True or False depending if the  value exists in the tree.
    def findexists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.findexists(val)

        if self.right == None:
            return False

        return self.right.findexists(val)

    # Then here I've added a method to print the values in the tree in the order of their keys
    # This is when a user wants to view the added data
    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals



