######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Bayesian Network CL: Clase donde se encontrará todas las funciones de esta
librería de redes bayesianas e interferencia probabilística.
"""
######################################################################################

class BayesianNetwork():
    def __init__(self) -> None:        
        self.nodes = {}
    
    def insert_node(self, node : str) -> None:        
        if node is not self.nodes:
            self.nodes[node] = []
    
    def insert_connection(self, node : str, node_to_connect = str) -> int:
        if node not in self.nodes:
            return -1
        
        if node_to_connect not in self.nodes:
            return 0
        
        self.nodes[node].append(node_to_connect)
        return 1
        
    def add_probs(self, probs : list) -> None:
        ...
        
    def show_nodes(self) -> str:
        info_nodes = ''
        for key, value in self.nodes.items():
            info_nodes += f'{key} --> {value}\n'
        return info_nodes
        
    def show_bayesian_network(self) -> str:
        ...
        
    def show_bayesian_network_and_probs(self) -> str:
        ...
        
    def query_prob(self, query : str) -> str:
        ...