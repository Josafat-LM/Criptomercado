import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('criptomonedas_filtradas.csv')

G = nx.Graph()
for index, row in df.iterrows():
    G.add_node(row['name'], category=row['category'])

# Añadir aristas basadas en categorías
categories = df['category'].unique()
for category in categories:
    nodes_in_category = df[df['category'] == category]['name'].tolist()
    for i in range(len(nodes_in_category)):
        for j in range(i + 1, len(nodes_in_category)):
            G.add_edge(nodes_in_category[i], nodes_in_category[j])

print(f'Número de nodos en el grafo: {G.number_of_nodes()}')
print(f'Número de aristas en el grafo: {G.number_of_edges()}')

# Visualizar el grafo
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Layout del grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, edge_color='gray', font_size=10, font_weight='bold')
plt.title('Grafo de Criptomonedas por Categoría')
plt.show()

#====================================================================
# Crear subgrafos para cada categoría
for category in categories:
    subgraph_nodes = df[df['category'] == category]['name'].tolist()
    subgraph = G.subgraph(subgraph_nodes)
    
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(subgraph, seed=42)
    nx.draw(subgraph, pos, with_labels=True, node_color='lightgreen', node_size=3000, edge_color='gray', font_size=10, font_weight='bold')
    plt.title(f'Grafo de Criptomonedas - Categoría: {category}')
    plt.show()
