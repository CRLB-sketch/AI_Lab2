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
    
    def add_nodes(self, all_nodes) -> None:
        for edge_1, edge_2 in all_nodes:
            if edge_1 not in self.nodes: self.nodes[edge_1] = []
            if edge_2 not in self.nodes: self.nodes[edge_2] = []
            self.nodes[edge_1].append(edge_2)
            
        nodes_count = {}
        for key, value in self.nodes.items():
            nodes_count[key] = 0
                                    
        for key, value in self.nodes.items():
            for v in value:
                nodes_count[v] += 1
                        
    def add_probs(self, probs : list) -> None:
        ...
        
    def show_bayesian_network(self) -> str:
        info_nodes = ''
        for key, value in self.nodes.items():
            info_nodes += f'{key} --> {value}\n'
        return info_nodes
                
    def show_bayesian_network_and_probs(self) -> str:
        info_nodes = ''        
            
        return info_nodes
        
    def inference_by_enumeration(self, query : str, e_variables : str, bn : object) -> float:
        ...
        
    def bayesian_network_complete(self) -> bool:
        return True
    