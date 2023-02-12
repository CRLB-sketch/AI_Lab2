import pytest
from bayesian_network_cl import BayesianNetwork
    
@pytest.mark.parametrize(
    "node, result_expected",
    [
        ('C', 'C --> []\n'),
        ('Z', 'Z --> []\n'),
        ('A', 'A --> []\n'),
        ('D', 'D --> []\n'),
        ('R', 'R --> []\n'),
    ]
)
def test_insert_nodes(node, result_expected):
    bn = BayesianNetwork()    
    bn.insert_node(node)
    assert result_expected == bn.show_nodes() # Only one node by node
    
def test_insert_many_nodes():
    bn = BayesianNetwork()
    
    bn.insert_node("B")
    bn.insert_node("E")
    bn.insert_node("A")
    
    expected = 'B --> []\n'
    expected += 'E --> []\n'
    expected += 'A --> []\n'
    
    actual = bn.show_nodes()
    assert expected == actual
    
def test_insert_connection_all_true():
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
    
    expected = "B --> ['A']\n"
    expected += "E --> ['A']\n"
    expected += "A --> ['J', 'M']\n"
    expected += "J --> []\n"
    expected += "M --> []\n"
    
    actual = bn.show_nodes()
    assert expected == actual