"""
Author: Mageza Shalom
Cohort: 2
Retake Assessment: 3
Part II : Circular Linked List
"""

def CountNumberOfNodes(self):
  # Here I will first create a node pointing to head
  node = self.head
  
  # Then I create a variable x which counts the nodes
  x = 0

  # If the node is not null I encrease x by one and move to the next node until null
  if (node != None):
    x += 1
    node = node.next
  while (node != self.head):
    x += 1
    node = node.next
    
  #Then Finally I will return the count of the nodes
  return x 
