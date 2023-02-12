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

    bn.insert_node("B")
    bn.insert_node("E")
    bn.insert_node("A")
    bn.insert_node("J")
    bn.insert_node("M")
    
    bn.insert_connection("B", "A")
    bn.insert_connection("E", "A")
    bn.insert_connection("A", "J")
    bn.insert_connection("A", "M")
        
    nodes = bn.show_nodes()
    print(nodes)    
    # -----------------------------------------------------------------------
    
    print(f'{"":#^100}')