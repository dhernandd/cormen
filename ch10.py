# Copyright 2017 Daniel Hernandez Diaz, Columbia University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ==============================================================================

## CH. 10: ELEMENTARY DATA STRUCTURES

class Node():
    """
    """
    def __init__(self, key, **kwargs):
        """
        """
        self.key = key
        for keyword in kwargs: setattr(self, keyword, kwargs[keyword])
        
    
class Stack(object):
    """
    """
    def __init__(self, last=None):
        """
        """
        self.last = last
    
    @classmethod
    def from_list(cls, L=[]):
        stack = Stack()
        for i, item in enumerate(L):
            node = Node(i, data=item)
            cls.push(stack, node)
        return stack

    def is_stack_empty(self):
        """
        """
        return True if self.last is None else False 
         
    def push(self, elem):
        """
        """
        if isinstance(elem, Node):
            if self.last is None:
                self.last = elem
                self.last.next_up = None
            else:
                current_last = self.last
                self.last = elem
                self.last.next_up = current_last
        else:
            try:
                node = Node(elem)
                self.push(node)
            except:
                assert False, 'Element is not a node, nor is \
                it an immutable that could be converted to an empty node.'
              
    def pop(self):
        if self.is_stack_empty():
            assert False, 'Underflow. Stack is empty.'
        else:
            current_last = self.last
            self.last = self.last.next_up
            return current_last
            
        
class Queue(object):
    """
    """
    def __init__(self, last=None, first=None):
        """
        """
        self.last = last
        self.first = first
        
    @classmethod
    def from_list(cls, L):
        """
        """
        queue = Queue()
        for i, item in enumerate(L):
            node = Node(i, data=item)
            cls.enqueue(queue, node)
        return queue
       
    def is_queue_empty(self):
        return True if self.first is None else False
    
    def enqueue(self, elem):
        """
        """
        if isinstance(elem, Node):
            if self.is_queue_empty():
                self.first = elem
                self.last = elem
                self.last.next_up = None
            elif self.first == self.last:
                self.first = elem
                self.last.next_up = self.first
            else:
                current_first = self.first
                self.first = elem
                current_first.next_up = self.first
        else:
            try:
                node = Node(elem)
                self.enqueue(node)
            except:
                assert False, 'Element is not a node, nor is \
                it an immutable that could be converted to an empty node.'
    
    def dequeue(self):
        """
        """
        if self.is_queue_empty():
            assert False, 'Underflow. Stack is empty.'
        elif self.first == self.last:
            elem = self.first
            self.first = self.last = None
            return elem
        else:
            elem = self.last
            self.last = self.last.next_up
            return elem
            

class LLNode(Node):
    """
    An element of a (doubly) linked list
    """
    def __init__(self, key, prev=None, nxt=None, **kwargs):
        """
        """
        Node.__init__(self, key, **kwargs)

        self.prev = prev
        self.nxt = nxt
        
    
    def __eq__(self, other):
        """
        This is to allow for removal
        """
        return self.key == other.key
        

class BTNode(Node):
    """
    """
    def __init__(self, key, parent=None, left=None, right=None, **kwargs):
        """
        """
        Node.__init__(self, key, **kwargs)
        
        self.parent = parent
        self.left = left
        self.right = right
        
    def has_child(self, loc):
        if loc == 'L':
            return False if self.left is None else True
        elif loc == 'R':
            return False if self.right is None else True
        else:
            assert False, 'Children must be either left or right. \
                            This code respects nonbinary children though.'


class RTNode(object):
    """
    """
    def __init__(self, key, parent=None, left_child=None, right_sibling=None, **kwargs):
        """
        """
        Node.__init__(self, key, **kwargs)
                
        self.parent = parent
        self.left_child = left_child
        self.right_sibling = right_sibling

        
    def has_child(self):
        return False if self.left is None else True
        

class LinkedList(object):
    """
    NTS: Sets seem to be the most appropriate python data type for this    
    """
    def __init__(self, first=None, last=None, keys_provided=False):
        """
        TODO: Add a constructor for the linked list from a python list.
        """
        self.keys_provided = keys_provided
        self.first = first
        self.last = last
        self.left_sentinel = LLNode(None)
        self.right_sentinel = LLNode(None, prev=self.left_sentinel)
        self.left_sentinel.nxt = self.right_sentinel
        
        self.Nb = 0
        self.Nf = 0

    def __repr__(self):
        if self.first is None:
            return None
        else:
            L = []
            cur_node = self.first
            while cur_node.key != None:
                L.append(cur_node.key)
                cur_node = cur_node.nxt
            return str(L) 
    
    def is_empty(self):
        return self.first is None
    
    def append_create(self, key=None, **kwargs):
        """
        Creates and appends an object at the end of the linked list.
        """
        if self.keys_provided and not key: assert False, 'A key must be provided for this node'
        if self.first is None:
            if not self.keys_provided: key = 'O'
            self.first = LLNode(key, prev=self.left_sentinel, 
                                nxt=self.right_sentinel, **kwargs)
            self.last = self.first
            self.left_sentinel.nxt = self.first
            self.right_sentinel.prev = self.first
        else:
            if not self.keys_provided:
                key = 'F' + str(self.Nf)
                self.Nf += 1 
            cur_last = self.last
            self.last = LLNode(key, prev=cur_last,
                               nxt=self.right_sentinel, **kwargs)
            cur_last.nxt = self.last
            self.right_sentinel.prev = self.last
            
    def append(self, node, replace_name=False):
        """
        Appends an arbitrary Node to the end of the linked list and adds the
        necessary properties.
        """
        if self.first is None:
            self.first = self.last = node
            self.first.prev = self.left_sentinel
            self.first.nxt = self.right_sentinel
        else:
            cur_last = self.last
            self.last = node
            node.prev = cur_last
            node.nxt = self.right_sentinel
            cur_last.nxt = self.last 
        if replace_name:
            self.last.key = 'F' + str(self.Nf)
        self.Nf += 1
            
    def insert(self, key, **kwargs):
        """
        TODO: Implement inserting.
        """
        pass
    
    def delete(self, key):
        """
        """
        print 'Linked List:', self.__repr__()
        if self.first is None:
            assert False, 'Key not found! (Linked List is empty)'
        else:
            cur_node = self.first
            while key != cur_node.key:
                print key
                if cur_node.key is None:
                    assert False, 'Key not found!'
                cur_node = cur_node.nxt

            # Once the key has been found, delete it. Some particular boundary
            # behavior.
            cur_node.prev.nxt, cur_node.nxt.prev = cur_node.nxt, cur_node.prev
            if cur_node == self.first:
                if cur_node == self.last:
                    self.first = self.last = None
                else:
                    self.first = self.first.nxt
            elif cur_node == self.last:            
                self.last = self.last.prev
            return cur_node
                            
    def find(self, key):
        """
        Finds a node with a given key scanning the linked list sequentially.
        """
        cur_node = self.first
        while key != cur_node.key:
            if cur_node.nxt == None:
                print 'Key not found!'
            cur_node = cur_node.nxt
        return cur_node


class BinaryTree(object):
    """
    A plain vanilla binary tree.
    
    This is a sort of useless data structure. Nevertheless, I will
    use this class as a base class for more complicated trees.
    """
    def __init__(self, root=None, keys_provided=False):
        """
        TODO: Add a constructor for the binary tree from a list.
        """
        self.keys_provided = keys_provided
        self.root = root
        
        self.nnodes = 0
                
    def get_subtree(self, node, keys_provided=False):
        return BinaryTree(node, keys_provided)
    
    def is_empty(self):
        return self.root is None
    
    def search(self, key, cur_node):
        """
        This is O(n) since it visits every node once.
        
        Better search methods will come for more sophisticated trees
        """
        if self.is_empty():
            assert False, 'Tree is empty!'
        cur_key = cur_node.key
        if cur_key == key:
            print 'Found!'
            return cur_node
        if cur_node.left: 
            node = self.search(key, cur_node.left)
            if node: return node
        if cur_node.right:
            node = self.search(key, cur_node.right)
            if node: return node
                    
    def add_root(self, key=None, **kwargs):
        """
        """
        self.nnodes += 1
        if not self.keys_provided: key = self.nnodes
        self.root = BTNode(key, **kwargs)
        
     
    def insert_leaf_create(self, parent_key, key=None, loc='L', **kwargs):
        """
        insert inserts children of parent_key with location loc.
        """
        parent_node = self.search(parent_key, self.root)
        if parent_node is None: assert False, 'Parent node does not exist.'
        if self.keys_provided and not key: 
            assert False, 'A key must be provided for this node'
        if parent_node.has_child(loc): 
            assert False, 'Overpopulation Error. Parent already has that child.'

        self.nnodes += 1
        if not self.keys_provided: key = self.nnodes
        node = BTNode(key, **kwargs)
        node.parent = parent_node
        if loc == 'L': parent_node.left = node
        if loc == 'R': parent_node.right = node
        return node
    
    



class RootedTree(object):
    """
    TODO: Implement
    """
    def __init__(self, keys_provided=False):
        """
        TODO: Add a constructor for the binary tree from a list.
        """
        self.keys_provided = keys_provided
        self.root = None

        self.node_dict = {}
        
    
    def insert_leaf(self, key=None, parent_key=None):
        """
        """
        pass


if __name__ == '__main__':
    
#     stack = Stack()
#     node1 = Node(1)
#     stack.push(node1)
#     stack.push(2)
#     print stack.pop().key
#     print stack.pop().key
    
#     ll = LinkedList()
#     ll.append_create(1)
#     ll.append_create(2)
#     ll.append_create(3)
#     print ll.first.nxt.nxt.key

    tree = BinaryTree()
    tree.add_root()
    node = tree.insert_leaf_create(1, loc='L')
    node = tree.insert_leaf_create(1, loc='R')
    node = tree.insert_leaf_create(2, loc='R')
    
    print 'H!'
    node = tree.search(3, tree.root)
    print 'Found key, parent key:', node.key, node.parent.key
    
#     
#     ll = LinkedList(keys_provided=True)
#     ll.append_create(1)
#     ll.append_create(2)
#     ll.append_create(3)
#     print ll.first.nxt.nxt.key

    
    
    
        