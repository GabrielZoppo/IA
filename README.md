# Inteligência Artifical

## Trabalho de implementação:
### Códigos Utilizados:
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
# Essa classe representa um grafo
import time


class Graph:
    # Inicia a classe
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Crie um gráfico não direcionado adicionando arestas simétricas
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Adicione um link de A e B de determinada distância,
    # e também adicione o link inverso se o gráfico não for direcionado
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Obtenha vizinhos ou um vizinho
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Retorna uma lista de nodos em um grafo
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


# Essa classe representa um nodo
class Node:
    # Inicialisa a classe
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compara nodos
    def __eq__(self, other):
        return self.name == other.name

    # Ordena nodos
    def __lt__(self, other):
        return self.f < other.f

    # Imprime nodos
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))


# Busca A*
def astar_search(graph, heuristics, start, end):
    # Cria listas para nodos abertos e fechados
    open = []
    closed = []
    # Cria um nodo inicial e um nodo final
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Adiciona o nodo inicial
    open.append(start_node)

    # Loop até a lista aberta estar vazia
    while len(open) > 0:
        # Classifique a lista aberta para obter o nó com o menor custo primeiro
        open.sort()
        # Obtenha o nó com o menor custo
        current_node = open.pop(0)
        # Adicione o nó atual à lista fechada
        closed.append(current_node)

        # Verifique se atingimos a meta, retorne o caminho
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Retornar caminho reverso
            return path[::-1]
        # Get vizinhos
        neighbors = graph.get(current_node.name)
        # Loop visinhos
        for key, value in neighbors.items():
            # Cria um nodo visinho
            neighbor = Node(key, current_node)
            # Verifique se o vizinho está na lista fechada
            if (neighbor in closed):
                continue
            # Calcular o custo do caminho completo
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Verifique se o vizinho está na lista aberta e se tem um valor de f inferior
            if (add_to_open(open, neighbor) == True):
                # Tudo é verde, adicione vizinho para abrir a lista
                open.append(neighbor)
    # Retornar Nenhum, nenhum caminho foi encontrado
    return None


# Verifique se um vizinho deve ser adicionado à lista aberta
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True


# Definindo o main
def main():

    # cria um grafo
    graph = Graph()

    # Cria conexões entre os grafos  (Distância Real)
    graph.connect('Frankfurt', 'Wurzburg', 111)
    graph.connect('Frankfurt', 'Mannheim', 85)
    graph.connect('Wurzburg', 'Nurnberg', 104)
    graph.connect('Wurzburg', 'Stuttgart', 140)
    graph.connect('Wurzburg', 'Ulm', 183)
    graph.connect('Mannheim', 'Nurnberg', 230)
    graph.connect('Mannheim', 'Karlsruhe', 67)
    graph.connect('Karlsruhe', 'Basel', 191)
    graph.connect('Karlsruhe', 'Stuttgart', 64)
    graph.connect('Nurnberg', 'Ulm', 171)
    graph.connect('Nurnberg', 'Munchen', 170)
    graph.connect('Nurnberg', 'Passau', 220)
    graph.connect('Stuttgart', 'Ulm', 107)
    graph.connect('Basel', 'Bern', 91)
    graph.connect('Basel', 'Zurich', 85)
    graph.connect('Bern', 'Zurich', 120)
    graph.connect('Zurich', 'Memmingen', 184)
    graph.connect('Memmingen', 'Ulm', 55)
    graph.connect('Memmingen', 'Munchen', 115)
    graph.connect('Munchen', 'Ulm', 123)
    graph.connect('Munchen', 'Passau', 189)
    graph.connect('Munchen', 'Rosenheim', 59)
    graph.connect('Rosenheim', 'Salzburg', 81)
    graph.connect('Passau', 'Linz', 102)
    graph.connect('Salzburg', 'Linz', 126)

    # Faça o gráfico sem direção, cria conexões simetricas
    graph.make_undirected()

    # Cria heuristica (distancia em linha reta, distancia em via aerea)
    heuristics = {}
    heuristics['Basel'] = 204
    heuristics['Bern'] = 247
    heuristics['Frankfurt'] = 215
    heuristics['Karlsruhe'] = 137
    heuristics['Linz'] = 318
    heuristics['Mannheim'] = 164
    heuristics['Munchen'] = 120
    heuristics['Memmingen'] = 47
    heuristics['Nurnberg'] = 132
    heuristics['Passau'] = 257
    heuristics['Rosenheim'] = 168
    heuristics['Stuttgart'] = 75
    heuristics['Salzburg'] = 236
    heuristics['Wurzburg'] = 153
    heuristics['Zurich'] = 157
    heuristics['Ulm'] = 0

    # Run the search algorithm
    inicio = time.time()
    path = astar_search(graph, heuristics, 'Frankfurt', 'Ulm')
    fim = time.time()
    print("Tempo de reação:" + str(fim - inicio))
    print(path)
    print()


# chamando o mai
if __name__ == "__main__": main()
~~~

### Tempo de Reação dos algoritmos de busca:
Grafos                  | Quantidade de iterações A*         | Quantidade de iterações BFS        |
:----------------------:|:----------------------------------:|:----------------------------------:|            			 		
1                       |7                                   |7                                    |			 		
2                       |5                                   |7                                    |			 		
3                       |7                                   |9                                    |

### Perguntas pedidas:
* A quantidade de nós em uma árvore influência no desempenho dos algoritmos de busca, de modo a tornar a busca sem informação melhor do que a busca com informação ou vice-versa?
* A posição de um nó objetivo dentro da árvore influência no desempenho dos algoritmos de busca com e sem informação?
* Com base nos resultados obtidos, dê exemplo de uma aplicação na qual seja mais vantajoso utilizar o algoritmo de busca sem informação.
* Com base nos resultados obtidos, dê exemplo de uma aplicação na qual seja mais vantajoso utilizar o algoritmo de busca com informação.

### Reposta das perguntas:
* Influencia, pois a busca em largura vai explorar vários nodos, sendo eles necessários ou não, podendo ser mais lento dependendo da situação. Umas das situações é quando o nodo objetivo está no final, sendo assim ele vai explorar todos os nodos, nessa situação a busca A* vai ser mais eficaz por não abrir certos nodos que vão ser desnecessários.

* Vai fazer diferença pois podemos entrar numa situação que vamos explorar mais nodos,podemos utilizar o objetivo no ultimo nodo a direita do grafo, ele vai ler todos os nodos do grafo inteiro, diferente de quando colocamos o objetivo em um dos nodos da esquerda, fazendo com que não testamos todos os nodos possíveis.


*  Varredura de informações em espaços pequenos.

*  Jogos que tenham obstáculos e busca de rotas rápidas em mapas.


## Trabalho 1 - Introdução ao aprendizado de máquina:
*  Tabela pedida:
			
Porte	 |Garras	        |Selvagem ou Doméstico |Peso em Kg  |Felino     | 
:-----:|:--------------:|:--------------------:|:----------:|:---------:|
Grande |	retrátil      |	Selvagem             |	120       |	Leão      |
Grande |	retrátil      |	Selvagem             |	300       |	Tigre     |
Pequeno|	retrátil      |	Selvagem             |	15        |	Cerval    |
Grande |	retrátil      |	Selvagem             |	30        |	Leopardo  |
Pequeno|	retrátil      |	Doméstico            |	5         |	Persa     |
Grande |	retrátil      |	Selvagem             |	50        |	Puma      |
Grande |	retrátil      |	Selvagem             |	60        |	Onça      |
Grande |	semi-retráteis|	Selvagem             |	30        |	Chita     |
Médio  |	retrátil      |	Doméstico            |	8         |	Maine Coon|
Pequeno|	retrátil      |	Doméstico            |	3         |	Siâmes    |

* Código Python:
~~~Python
from sklearn import tree

pequeno = 0
medio = 1
grande = 2

retratil = 0
semi_retratil = 1

selvagem = 0
domestico = 1

Leão = 0
Tigre = 1
Cerval = 2
Leopardo = 3
Persa = 4
Puma = 5
Onça = 6 
Chita = 7
Maine_Coon = 8
Siâmes = 9

breed = [[grande,retratil, 120, selvagem], [grande, retratil, 300, selvagem], [pequeno, retratil, 15, selvagem], [grande,retratil, 30, selvagem], [pequeno,retratil, 5, domestico], 
         [grande,retratil, 50, selvagem], [grande,retratil, 60, selvagem], [grande,semi_retratil, 30, selvagem], [medio,retratil, 8, domestico], [pequeno,retratil, 3, domestico]]
result = [Leão, Tigre, Cerval, Leopardo, Persa, Puma, Onça, Chita, Maine_Coon, Siâmes]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(breed, result)

porte = input("Entre com o porte (0 - Pequeno / 1 - Média / 2 - Grande): ")
garra = input("Entre com o tipo de  garra (0 - retratil / 1 - semi-retratil): ")
peso = input("Entre com o peso: ")
selvagem = input("Entre se é selvagem ou doméstico (0 - Selvagem / 1 - Domestico): ")

resultadoUsuario = clf.predict([[porte, garra, peso, selvagem]])

if resultadoUsuario == 0:
    print("É um leão!")
elif resultadoUsuario == 1:
    print("É um tigre!")
elif resultadoUsuario == 2:
    print("É um cerval!")
elif resultadoUsuario == 3:
    print("É um Leopardo!")
elif resultadoUsuario == 4:
    print("É um Persa!")
elif resultadoUsuario == 5:
    print("É um Puma!")
elif resultadoUsuario == 6:
    print("É um Onça!")
elif resultadoUsuario == 7:
    print("É um Chita!")     
elif resultadoUsuario == 8:
    print("É um Maine Coon!")            
else:
    print("É um Siâmes!")
~~~

* Verificação de Resultado:
  * 1º Teste:
    porte = grande 
    garra = retratil
    peso = 200
    selvagem = selvagem
    **É um Leão!**
  
  * 2º Teste:
    porte = grande 
    garra = retratil
    peso = 310
    selvagem = selvagem
    **É um Tigre!**
    
   * 3º Teste:
    porte = medio 
    garra = retratil
    peso = 5
    selvagem = domestico
    **É um Maine Coon!**
  
   * 4º Teste:
    porte = Grande 
    garra = semi_retratil
    peso = 40
    selvagem = selvagem
    **É um Chita!**
