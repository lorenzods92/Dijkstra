
'''Test module for Dijkstra algorithm'''

import unittest
import network as nt
import dijkstra as dk
import networkx as nx

class TestDijkstra(unittest.TestCase):
    
    def test_path(self):
        '''Check if results is equal with the one from networkx module, 
        random graph and start node changed for every node in vertex list'''
        #input
        n_vertex = 10
        seed = 3
        max_dist = 10
        density = 7
        
        #creates vertex list
        vertex_list = nt.create_vertex_list(n_vertex)
        #end node fixed
        end_node = "G"

        #tests changing starting point
        for vertex in vertex_list:
            start_node = vertex
            
            #creates net, distance matrix
            net = nt.create_rand_net(vertex_list, max_dist, seed, density)
            #Solve Dijkstra
            table = dk.solve_dijkstra(start_node, end_node, net, vertex_list)
            my_path = dk.return_shortest_path(table, start_node, end_node)
            
            #creates edges as tuples for networkx module input
            edges = nt.create_edges_from_net(net, vertex_list)
            #creates network from networkx
            G = nt.create_network_G_graph(edges)
    
            nx_path = nx.dijkstra_path(G, start_node, end_node)
            
            self.assertEqual(my_path, nx_path, f"start_node ={start_node}")


if __name__ == '__main__':
    unittest.main()