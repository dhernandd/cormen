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

## CH. 10: HASH tables

# TODO: Implement multiplication hashing
# TODO: Implement Universal hashing
# TODO: Implement open addressing
# TODO: Implement perfect hashing

from ch10 import Node, LinkedList


class HashTable(object):
    """
    """
    def __init__(self, hash_size=7919):
        """
        """
        self.hash_size = hash_size
        self.hash_table = [None]*self.hash_size
                
    def hash(self, item):
        """
        """
        try:
            hash_string = str(item.key) if isinstance(item, Node) else item
            value_to_hash = sum([ord(c) for c in hash_string])
            hash_key = value_to_hash % self.hash_size
            return hash_key
        except:
            assert False, 'Hashing error.'
        
    def chain_hash_insert(self, item):
        """
        """
        if isinstance(item, Node):
            hash_key = self.hash(item)
            if self.hash_table[hash_key] is None:
                ll = LinkedList(keys_provided=True)
                self.hash_table[hash_key] = ll
            else:
                ll = self.hash_table[hash_key]
            ll.append(item)
        else:
            try:
                node = Node(item)
                self.chain_hash_insert(node)
            except:
                assert False, 'Element is not a node, nor is \
                it an immutable that could be converted to an empty node.'
            
    def chain_hash_search(self, key):
        """
        """
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is None:
            print 'Element not in the hash table!'
        else:
            this_ll = self.hash_table[hash_key]
            node = this_ll.find(key)
            return node
        
    def chain_hash_delete(self, key):
        """
        """
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is None:
            print 'Element not in the hash table!'
        else:
            try:
                this_ll = self.hash_table[hash_key]
                this_ll.delete(key)
                print 'Key deleted.'
                if this_ll.is_empty():
                    del self.hash_table[hash_key]
                    print 'Entry deleted from the hash table'
            except:
                print 'Element not in the hash table!'


if __name__ == '__main__':
    H = HashTable()
    for c in ['hola', 'mundo', 'yeah']:
        H.chain_hash_insert(c)
        
    node = H.chain_hash_search('hola')
    print node.key
    H.chain_hash_delete('mundo')
    H.chain_hash_delete('mundo')