# Inteligência Artifical

## Código python Busca em largura:
~~~python
#declaração das bibliotecas
import time

#declaração dos grafos
grafo = [[2, 1],
         [5, 4, 0],
         [3, 0],
         [7, 5, 2],
         [6, 1],
         [8, 6, 3, 1],
         [10, 5, 4],
         [11, 3],
         [11, 10, 5],
         [10, 5, 4],
         [11, 8, 6],
         [10, 8, 7]]

#declaração da função buscaLargura
def buscaEmLargura(origem, destino):
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

#chamando a função
nosVisitados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
origem = 0
destino = 11

buscaEmLargura(origem, destino)
~~~
