# Laboratorio #2 - Redes Bayesianas

Universidad del Valle de Guatemala

Inteligencia Artificial - Sección 20

# Instalación

```bash
pip install
```

# Comandos y uso de la libreria

## - Llamar/Instanciar la Red Bayesiana

```python
from bayesian_network_cl import BayesianNetwork

bn = BayesianNetwork()
```

## - Agregar nodos

```python
add_nodes(self, all_nodes : list) -> None
```

## - Agregar probabilidades en un nodo

```python
add_probs(self, node: str, probs : list) -> None
```

## - Mostrar la Red Bayesiana

```python
show_bayesian_network(self) -> str
```

## - Mostrar la Red Bayesiana y sus probabilidades

```python
show_bayesian_network_and_probs(self) -> str
```

## - Verificar si el arbol bayesiano esta completo

```python
inference_by_enumeration(self, **conditions) -> float
```

## - Inferencia Probabilistica

```python
bayesian_network_complete(self) -> bool
```
