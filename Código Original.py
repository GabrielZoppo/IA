import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
arquivo = pd.read_csv('D:/Users/usuario/Desktop/heart.csv')


arquivo['output'] = arquivo['output'].replace('Chance Baixa', 0)
arquivo['output'] = arquivo['output'].replace('Chance Alta', 1)
print("\n", arquivo.head())


y = arquivo['output']
x = arquivo.drop('output', axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

modelo = ExtraTreesClassifier()
print("\n", modelo.fit(x_treino, y_treino))

modelo1 = RandomForestClassifier(max_depth=100, random_state=0)
print("\n", modelo1.fit(x_treino, y_treino))

modelo2 = GaussianNB()
print("\n", modelo2.fit(x_treino, y_treino))

resultados = modelo.score(x_teste, y_teste)
resultados = resultados*100
print("\nPrecisão Arvore de busca: " + str(resultados) + "%")

resultados1 = modelo1.score(x_teste, y_teste)
resultados1 = resultados1*100
print("\nPrecisão Floresta Aleatória:" + str(resultados1) + "%")

resultados2 = modelo2.score(x_teste, y_teste)
resultados2 = resultados2*100
print("\nPrecisão Naive Bayes:" + str(resultados2) + "%")
