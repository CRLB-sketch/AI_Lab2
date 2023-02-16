######################################################################################
_author_ = "Cristian Fernando Laynez Bachez - 201281"
_copyright_ = "Universidad el Valle de Guatemala, Inteligencia Artifical 2023"
_status_ = "Student of Computer Science"

"""
Main: Clase Principal

Esta clase se encargará solamente de realizar pruebas para la clase
de redes bayesianas
"""
######################################################################################

from bayesian_network_cl import BayesianNetwork

if __name__ == "__main__":
    print(f'{"":#^100}')
    print(f'{" Inteligencia Artificial - Laboratorio 2 ":#^100}')

    # -----------------------------------------------------------------------    
    bn = BayesianNetwork()
    
    bn.add_nodes([("B", "A"), ("E", "A"), ("A", "J"), ("A", "M")])
            
    nodes = bn.show_bayesian_network()
    print(nodes)    
    bs_and_probs = bn.show_bayesian_network_and_probs()
    print(bs_and_probs)
    # -----------------------------------------------------------------------
    
    print(f'{"":#^100}')
    