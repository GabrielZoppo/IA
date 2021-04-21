# Inteligência Artifical

## Código python Busca em largura:
~~~python
#declaração das bibliotecas
import time

#declaração da função buscaLargura
def buscaEmLargura(grafo, origem, destino):
    fila = []
    fila.append(origem)

    while len(fila) > 0:
        inicio = time.time()
        no = fila.pop(0)
        nosVisitados[no] = 1

        if no == destino:
            print("chegou ao destino")
            fim = time.time()
            print("Tempo de reação: %f Segundos " % (fim - inicio))
            break
        for n in grafo[no]:
            if nosVisitados[n] == 0:
                nosVisitados[n] = 1
                fila.append(n)
                
#declaração dos grafos
grafo1 =  [ [1],           # Vizinhos do vértice 0.
          [2, 3],        # Vizinhos do vértice 1.
          [1, 4],        # Vizinhos do vértice 2.
          [0],           # Vizinhos do vértice 3.
          [1]            # Vizinhos do vértice 4.
          ]

grafo2 =  [ [1, 2 ],           # Vizinhos do vértice 0.
          [2, 3],        # Vizinhos do vértice 1.
          [0, 1, 2, 4],        # Vizinhos do vértice 2.
          [1, 4],           # Vizinhos do vértice 3.
          [2, 3]            # Vizinhos do vértice 4.
          ]

grafo3 =  [ [1, 2, 3],           # Vizinhos do vértice 0.
          [0, 2, 3],        # Vizinhos do vértice 1.
          [0, 1, 4],        # Vizinhos do vértice 2.
          [0, 4],           # Vizinhos do vértice 3.
          [2]            # Vizinhos do vértice 4.
          ]
          
#chamando a função
nosVisitados = [0, 0, 0, 0, 0]
origem = 0
destino = 4

buscaEmLargura(grafo1, origem, destino)
~~~
## Tempo de Reação do busca em largura:
Grafos                  | Tempo de reação            |
:----------------------:|:--------------------------:|             			 		
Grafo 1                 |0.000031 µs                 |			 		
Grafo 2                 |0.000039 µs                 |			 		
Grafo 3                 |0.000036 µs                 |

## Código python Busca A*:
~~~python

~~~

## Tempo de Reação da Busca A*:
Grafos                  | Tempo de reação |
:----------------------:|:---------------:|             			 		
Grafo 1                 |                 |			 		
Grafo 2                 |                 |			 		
Grafo 3                 |                 |


