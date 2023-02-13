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
        
    probs = {
        "B": [0.001],
        "E": [0.002],
        "A": [0.95, 0.94, 0.29, 0.001],
        "J": [0.90, 0.05],
        "M": [0.70, 0.01],
    }
    
    '''
    ++++++++++++++++++++++++++++++++++
    P(B) = 0.001
    ++++++++++++++++++++++++++++++++++
    
    ++++++++++++++++++++++++++++++++++
    P(E) = 0.002
    ++++++++++++++++++++++++++++++++++
    
    ++++++++++++++++++++++++++++++++++
    B       E       P(A)
    t       t       0.95
    t       f       0.94
    f       t       0.29
    f       f       0.001
    ++++++++++++++++++++++++++++++++++
    
    ++++++++++++++++++++++++++++++++++
    A       P(J)
    t       0.90
    f       0.05
    ++++++++++++++++++++++++++++++++++
        
    ++++++++++++++++++++++++++++++++++
    A       P(M)
    t       0.70
    f       0.01
    ++++++++++++++++++++++++++++++++++
    '''
        
    nodes = bn.show_bayesian_network()
    print(nodes)    
    bs_and_probs = bn.show_bayesian_network_and_probs()
    print(bs_and_probs)
    # -----------------------------------------------------------------------
    
    print(f'{"":#^100}')
    