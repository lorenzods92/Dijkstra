'''Main module'''


import sys
import network as nt
import dijkstra as dk
import networkx as nx

from typing import Type



def main(n_vertex:int, max_dist: int, seed, density):
    
    '''Funtion that creates the network, returns net, edges and adiajency dict'''
    #creates vertex list
    vertex_list = nt.create_vertex_list(n_vertex)
        
    #creates net, distance matrix
    net = nt.create_rand_net(vertex_list, max_dist, seed, density)
    #creates edges as tuples for networkx module input
    edges = nt.create_edges_from_net(net, vertex_list)
    #creates dictionary with adjacency
    adj_dict = nt.create_adjacency_dict(edges, vertex_list)
    #creates network from networkx
    G = nt.create_network_G_graph(edges)
    
    #Get input
    start_node, end_node = get_input(vertex_list)
    
    #Solve Dijkstra
    table = dk.solve_dijkstra(start_node, end_node, net, vertex_list)
    path = dk.return_shortest_path(table, start_node, end_node)
    
        
    #print Dijkstra form networkx
    print('NX result: ', nx.dijkstra_path(G, start_node, end_node))
    print('My result: ', path)

    
def get_input(vertex_list: list) -> tuple:
    '''Get input from keyboard, returns start and end node'''
    start_node = input(f"Please enter start node from list {vertex_list}:\n")
    end_node = input(f"Please enter end node:\n")
    
    if start_node not in vertex_list or end_node not in vertex_list:
        raise ValueError('start/end nodes not in list:\n')
        
    return start_node, end_node
    
  
if __name__ == "__main__":
    n_vertex = 12
    max_dist = 6
    density = 12 # the bigger the less dense is the graph
    seed = 3
    
    print ("Number of arguments:", len(sys.argv), "arguments")
    print ("Argument List:", str(sys.argv))
    
    main(n_vertex, max_dist, seed, density)
    
    
    
    
    