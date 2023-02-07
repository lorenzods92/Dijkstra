'''Module to solve a grph using Dijkstra algorithm'''
from typing import List
from typing import Type
import math

class ScoreNode:
    '''Class to handle node'''

    def __init__(self, name, dist = math.inf, via = None, visited = False)    :
        self.name = name
        self.dist = dist
        self.via = via
        self.visited = visited
        
        
    def __repr__(self):
        return f"name: {self.name}, dist: {self.dist}, via: {self.via}, visited: {self.visited}"
    
    def __lt__(self, other):
        return self.dist < other.dist
    
    def __eq__(self, other):
        return self.name == other.name
  
      
class IndexedNet:
    '''Class to handle net and vertex'''
    
    def __init__(self, net, vertex_list):
        self.net = net
        self.vertex_list = vertex_list
        
    def get_index_from_vertex(self, vertex) -> int:
        return self.vertex_list.index(vertex)
    
    def get_vertex_from_index(self, index) -> str:
        return self.vertex_list[index]
        
    def get_neighbors(self, node) -> dict:
        
        neighbors = {}
        index = self.get_index_from_vertex(node.name)
        net_row = self.net[index]
        
        for j, elem in enumerate(net_row):
            if elem > 0:
                neighbor_vertex = self.get_vertex_from_index(j)
                neighbor_dist = net_row[j]
                neighbors[neighbor_vertex] = neighbor_dist
                
        return neighbors
        
     

def solve_dijkstra(start_node, end_node, net: List[int], vertex_list: list):
    ''' Solve Dijkstra shortest path from start_node to end node, returns
    the table with vertex, distance, via, visited'''
    
    #Initialize score_nodes
    score_nodes = []
    for node in vertex_list:
        if node == start_node:
            score_nodes.append(ScoreNode(node, dist = 0, via = node))
        else:
            score_nodes.append(ScoreNode(node))
     
    
    #initialize indexed net
    ind_net = IndexedNet(net, vertex_list)
    #initialize summary table
    table = []
            
    
    while score_nodes:
        #order score_nodes by distance
        score_nodes = sorted(score_nodes)
        #get the closest
        current = min(score_nodes)
        
        #get neighbors/distances
        neighbors = ind_net.get_neighbors(current)
        
        #update score distances and vias
        via = current.name
        cum_dist = current.dist
        current.visited = True
        for name, dist in neighbors.items():
            #find node  and check if not visited
            for node in score_nodes:
                if node.name == name and not node.visited:
                    if node.dist > (cum_dist + dist):
                        #update values in score_nodes
                        node.dist = cum_dist + dist
                        node.via = via
            
        
        table.append(score_nodes.pop(0))
        
        
    return table

def return_shortest_path(table: list, start_node: str, end_node: str) -> list:
    '''Returns shortest path with vertexes in the correct sequence
    ex: ["A","C","D"]. List in input is a list of ScoreNodes objects'''
    
    #Case of trivial solution
    if start_node == end_node:
        return [start_node]
    
    #path initialization whith end node
    first = find_node_in_list(table, end_node)
    path = [first.name]
    nxt = first.via
    
    while start_node != nxt:
        #iterate trough list
        current = find_node_in_list(table, nxt)
        path.append(current.name)
        nxt = current.via
    
    #append starting node
    path.append(nxt)
    
    #reverse path from beginning to end
    path.reverse()
    
    return path


def find_node_in_list(lst: list, node_name: str) -> Type[ScoreNode]:
    '''Return ScoreNode if founds name in list'''
    for node in  lst:
        if node.name == node_name:
            return node
        
        
    

    

