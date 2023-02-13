import pytest
from bayesian_network_cl import BayesianNetwork
    
def test_insert_connection_all_true():
    bn = BayesianNetwork()
    
    bn.add_nodes([("B", "A"), ("E", "A"), ("A", "J"), ("A", "M")])
    
    expected = "B --> ['A']\n"
    expected += "A --> ['J', 'M']\n"
    expected += "E --> ['A']\n"
    expected += "J --> []\n"
    expected += "M --> []\n"
    
    actual = bn.show_nodes()
    assert expected == actual