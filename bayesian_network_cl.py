######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Bayesian Network CL: Clase donde se encontrará todas las funciones de esta
librería de redes bayesianas e interferencia probabilística.
"""
######################################################################################

import itertools

class BayesianNetwork():
                
    def __init__(self) -> None:         
        self.nodes = {}
        self.probs = {}
    
    def add_nodes(self, all_nodes) -> None:
        temp_nodes = {}
        for edge_1, edge_2 in all_nodes:
            if edge_1 not in self.nodes: self.nodes[edge_1] = []
            if edge_2 not in self.nodes: self.nodes[edge_2] = []
            self.nodes[edge_1].append(edge_2)
                    
        nodes_count = {}
        for key, value in self.nodes.items():
            if key not in nodes_count:
                nodes_count[key] = 0
                                    
        for key, value in self.nodes.items():
            for v in value:
                nodes_count[v] += 1

        print('----------------------')
        for key, value in self.nodes.items():
            print(f'{key} & {value} & {nodes_count[key]}')
        print('----------------------')

    def add_probs(self, probs : list) -> None:
        ...
        
    def show_bayesian_network(self) -> str:
        info_nodes = ''
        for key, value in self.nodes.items():
            info_nodes += f'{key} --> {value}\n'
        return info_nodes
                
    def show_bayesian_network_and_probs(self) -> str:
        info_nodes = ''

        # We are going to test something
        testing = {}
        for key, value in self.nodes.items():
            for v in value:
                print(f'P({v} | {key})')
                if v not in testing:
                    testing[v] = [key]
                else:
                    testing[v].append(key)
            
        for key, value in self.nodes.items():
            if key not in  testing:
                testing[key] = []
    
        print(testing)

        set_probs = {}
        for key, value in testing.items():
            n = 2 ** len(value)
            print(f'{key} and {value} # {n} and {len(value)}')
            table = list(itertools.product([True, False], repeat=len(value)))
            print(table)
        
        return info_nodes
        
    def inference_by_enumeration(self, **conditions) -> float:
        print('+++++++++++++++++++++++++')
        for i, j in conditions.items():
            print(f'{i} and {j}')
        print('+++++++++++++++++++++++++')
        
        return
        
    def bayesian_network_complete(self) -> bool:
        return True
    