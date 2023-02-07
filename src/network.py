'''Module to create the network-graph'''

import string
import random
import networkx as nx
# import matplotlib.pyplot as plt



def create_vertex_list(n_vertex: int) -> list:
    '''Cretae vertexes list, max 52 vertexes'''

    vertex_list = list(string.ascii_uppercase + string.ascii_lowercase)
    vertex_list = vertex_list[0:n_vertex]
    return vertex_list


def create_rand_net(vertex_list: list, max_dist: int, seed: int, density: int) -> list:
    '''Create random network and return it as a distance matrix of lists'''
       
    #Initialize net/graph
    net = [[0 for vertex in vertex_list] for vertex in vertex_list]
    
    #build the net
    random.seed(seed)
    for i in range(len(vertex_list)):
        for j in range(i, len(vertex_list)):
            if i != j:
                distance = random.choice([i for i in range(0, max_dist)] +
                                         [0 for i in range(0, density)])
                net[i][j] = distance
                net[j][i] = distance
        
    return net


def create_edges_from_net(net: list, vertex_list: list):
    '''Create list of tuple of edges ex: (NodeA, nodeB, distance)'''
    
    if len(net) != len(vertex_list):
        raise ValueError('net rows should be equal to vertexes number')
    
    edges = []
    
    for i, row in enumerate(net):
        for j, value in enumerate(row):
            if value != 0:
                start_node = vertex_list[i]
                end_node = vertex_list[j]
                distance = net[i][j]
                edge = (start_node, end_node, distance)
                edges.append(edge)
                
    return edges


def create_adjacency_dict(edges: list, vertex_list: list) -> dict:
    '''Created adjacency dictionary, specifying in a set which vertex is connected'''
    
    adj_dict = {vertex: set() for vertex in vertex_list}
    
    for edge in edges:
        adj_dict[edge[0]].add(edge[1])
        adj_dict[edge[1]].add(edge[0])
        
        
    return adj_dict

 
def create_network_G_graph(edges: list):
    '''Creates network with networkx module'''
    
    # plt.figure(figsize=(7,7))
    
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels = True)
    # edge_weight = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
    
    # plt.savefig('graph.png', dpi = 200)
    # plt.show()
    
    return G

def print_graph_info(vertex_list: list, net: list, edges: list):
    '''Prints graph infos'''
    
    print('vertex_list: ', vertex_list)
    print('net: ', net)
    print('edges: ', edges)
    
    
    