#!/usr/bin/env python
# coding: utf-8

# In[6]:


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def largestValues(self, root):
        if not root:
            return []

        result = []  # Initialize a list to store the largest values in each level
        queue = [root]  # Initialize a queue for level-order traversal

        while queue:
            level_max = float("-inf")  # Initialize the maximum value for the current level

            # Process all nodes in the current level
            for _ in range(len(queue)):
                node = queue.pop(0)  # Dequeue the front node

                # Update the maximum value for the current level
                level_max = max(level_max, node.val)

                # Enqueue the child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the maximum value of the current level to the result
            result.append(level_max)

        return result


# In[7]:


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)


# In[8]:


solution = Solution()
result = solution.largestValues(root)


# In[9]:


result


# In[ ]:




