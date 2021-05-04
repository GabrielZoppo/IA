# Inteligência Artifical

## Códigos Utilizados:
* Busca em largura:
~~~Python
import time
grafo = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visitado = [] # Lista pros nodos visitados.
queue = []     #inicie a fila

def BuscaEmLargura(visitado, grafo, nodo): #função pra busca em largura
  inicio = time.time() # começar o timer
  visitado.append(nodo)
  queue.append(nodo)

  while queue:          # Criando um loop para visitar cada nodo
    m = queue.pop(0) 
    print (m, end = " ")
    for visinho in grafo[m]:
      if visinho not in visitado:
        visitado.append(visinho)
        queue.append(visinho)
  fim = time.time() # terminar o timer

  print("\n" + "Tempo de reação: " +str(fim-inicio)) # imprimir na tela o tempo de reação

# Código para chamada
print("Seguindo a busca em largura")
BuscaEmLargura(visitado, grafo, '5')    # Chamando a função busca em largura
~~~

* Código do Busca A*:
~~~Python

~~~

## Tempo de Reação dos algoritmos de busca:
Grafos                  | Tempo de reação da Busca em largura| Tempo de reação da Busca A*        |
:----------------------:|:----------------------------------:|:----------------------------------:|            			 		
1                       |                                    |                                    |			 		
2                       |                                    |                                    |			 		
3                       |                                    |                                    |

## Perguntas pedidas:
* A quantidade de nós em uma árvore influência no desempenho dos algoritmos de busca, de modo a tornar a busca sem informação melhor do que a busca com informação ou vice-versa?
* A posição de um nó objetivo dentro da árvore influência no desempenho dos algoritmos de busca com e sem informação?
* Com base nos resultados obtidos, dê exemplo de uma aplicação na qual seja mais vantajoso utilizar o algoritmo de busca sem informação.
* Com base nos resultados obtidos, dê exemplo de uma aplicação na qual seja mais vantajoso utilizar o algoritmo de busca com informação.

## Reposta das perguntas:
* 
* 
* 
* 
