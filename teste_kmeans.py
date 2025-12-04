import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# 1. Dados fornecidos
data = """
197.0,52.0,42.0,5.6,23.41
146.0,22.0,37.0,5.9,32.23
165.0,33.0,48.0,4.5,19.27
193.0,32.0,37.0,5.4,21.34
122.0,26.0,45.0,3.4,20.68
120.0,38.0,44.0,4.6,25.85
142.0,13.0,20.0,5.2,32.77
100.0,23.0,60.0,3.0,19.09
164.0,39.0,44.0,4.6,22.61
131.0,43.0,41.0,5.1,25.29
143.0,39.0,48.0,3.9,23.61
83.0,25.0,40.0,4.2,24.38
122.0,21.0,40.0,4.5,29.81
142.0,27.0,50.0,3.5,23.89
121.0,34.0,40.0,4.6,31.76
117.0,34.0,52.0,3.1,19.05
109.0,23.0,50.0,5.4,25.87
153.0,33.0,41.0,5.4,20.97
190.0,23.0,52.0,5.1,18.01
114.0,26.0,41.0,4.5,40.31
169.0,26.0,42.0,4.9,22.41
"""

# Criar DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data), sep=',', header=None)
df.columns = ['S. horizontal', 'abdominal', 'flexibilidade', 'arremessoMB', 'IMC']

print("--- Dados Carregados ---\n")
print(df.head())
print("\n" + "="*50)

# 2. Padronização dos Dados
# Isso é crucial para que o K-means não seja dominado por métricas com valores altos (ex: Salto Horizontal)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# 3. Aplicar K-means (K=4 para corresponder aos seus 4 perfis desejados)
K = 4
kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# 4. Obter e Interpretar os Centróides
centroids_scaled = kmeans.cluster_centers_

# Inverter a Padronização para visualizar os centróides na escala original
centroids_original = scaler.inverse_transform(centroids_scaled)

centroids_df = pd.DataFrame(centroids_original, 
                            columns=df.columns[:-1]) # df.columns[:-1] remove a coluna 'Cluster'
centroids_df.index.name = 'Cluster ID'

print("### Centróides K-means (Escala Original) ###")
print("Os valores abaixo representam a MÉDIA de cada cluster e definem os perfis que o K-means encontrou.")
print("="*50)
print(centroids_df.round(2))
print("="*50)

# 5. Contagem de Membros em Cada Cluster
cluster_counts = df['Cluster'].value_counts().sort_index()
print("\nContagem de Amostras por Cluster:")
print(cluster_counts)