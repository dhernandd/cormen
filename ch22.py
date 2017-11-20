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

# CH. 22: ELEMENTARY GRAPH ALGORITHMS

from ch10 import Node

class GNode(Node):
    """
    """
    def __init__(self, key, neighbor_keys=[], **kwargs):
        """
        """
        Node.__init__(self, key, **kwargs)
        self.neighbor_keys = neighbor_keys
        print 'Key, Neighbors:', key, neighbor_keys
        
        
class GEdge(object):
    """
    """
    def __init__(self, edge_tuple, **kwargs):
        """
        """
        self.edge_tuple = edge_tuple
        for key in kwargs: setattr(self, key, kwargs[key])
        

class Graph(object):
    """
    """
    def __init__(self, nodedict, edgedict=None, **kwargs):
        """
        nodedict:     A very basic representation of a graph to be replaced by
        an adjacency matrix or an adjacency listdictionary of nodes where the
        keys are the node keys and the values are tuples where the first element
        is a list of the keys to the nodes this node is linked to and the second
        element is the data of that node.
        """
        self.nodedict = nodedict
        if edgedict is None: self._generate_edgedict()
        else: self.edgedict = edgedict 
        for key in kwargs: setattr(self, key, kwargs[key])
                
        # Create the graph representation, both an adjacency list and an adjacency matrix
        self._create_adjacency_list()


    def _generate_edgedict(self):
        """
        This method generates a dict of tuples:data, each representing an edge.
        This dict is required by self._create_adjacency_list()
        
        [Adapted from https://www.python-course.eu/graphs_python.php] 
        """
        self.edgedict = {}
        for node in self.nodedict:
            for neighbor in self.nodedict[node][0]:
                self.edgedict[(node, neighbor)] = {}


    def _create_adjacency_list(self):
        """
        Creates the adjacency list representation of the graph.
        
        This function "cheats", meaning that I use a python dict for fast access
        to nodes given their keys. Otherwise I would have to implement a search
        within a list of nodes to find each node's neighbor, a O(n^2) endeavor.
        This is of course unnecessary if the graph was defined already via an
        adjacency matrix. Bottom line, cheating is allowed only to construct the
        data structure.
        
        The adjacency list is stored as a property of the Graph instance. In
        addition, each node is added a property consisting of its own adjacency
        list. This ensures fast access to the adjacency list of a given node.
        Otherwise, we would have to search for it within the graph adjacency list.
        """
        node_dict = {}
        # First create a dict of nodes
        for nodekey in self.nodedict:
            this_node_neighbor_keys = self.nodedict[nodekey][0]
            this_node_data = self.nodedict[nodekey][1]
            this_node = GNode(nodekey, neighbor_keys=this_node_neighbor_keys, 
                              **this_node_data)
            node_dict[nodekey] = this_node
        self.node_list = node_dict.values()
        
        # Now define the adjacency list.   
        self.adjacency_list = []
        for node in self.node_list:
            this_node_list = []
            for neighbor_key in node.neighbor_keys:
                print node.key, neighbor_key
                edge_key = (node.key, neighbor_key)
                edge_data = self.edgedict[edge_key]
                this_edge = GEdge(edge_key, **edge_data)
                this_node_list.append((node_dict[neighbor_key], this_edge))
            node.adj_list = this_node_list
            self.adjacency_list.append(this_node_list)
    
    
    
    def breadth_first_search(self, source, target_key=None):
        """
        Implements a BFS algorithm looking for target_key in case it is given. 
        Adds BFS properties to node objects.
        
        If target_key is None, BFS goes on to "discover" every vertex that is
        reachable from source
        """ 
        print '\nStarting BFS. Searching for target_key:', target_key
        for node in self.node_list:
            if node.key == source:
                node.color = 'gray'
                node.distance = 0
                node.pred = None
                source_node = node
            else:
                node.color = 'white'
                node.distance = 'inf'
                node.pred = None
        
        from ch10 import Queue
        Q = Queue()
        Q.enqueue(source_node)
        
        while not Q.is_queue_empty():
            node = Q.dequeue()
            for neighbor, _ in node.adj_list:
                if neighbor.color == 'white':
                    neighbor.color = 'gray'
                    neighbor.distance = node.distance + 1
                    neighbor.pred = node
                    if neighbor.key == target_key:
                        print 'Item found!'
                        print 'Distance from source:', neighbor.distance
                        return neighbor 
                    Q.enqueue(neighbor)
            node.color = 'black'
                
        for node in self.node_list:
            print node.key, node.color, node.distance,
            if node.pred is not None:
                print node.pred.key,
            print '\n',
            
        
    def depth_first_search(self, source, item=None):
        """
        Implements a DFS algorithm looking for item in case it is given. 
        Adds DFS properties to node objects
        
        If item is None, DFS goes on to "discover" every vertex that is
        reachable from source
        """ 
        
    
if __name__ == '__main__':
    d = {'A' : (['B'], {}), 'B' : (['A', 'C'], {}), 'C' : (['B'], {}) }
    g1 = Graph(d)
    
    g1.breadth_first_search('B')

    
            
                