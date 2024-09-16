import dask.dataframe as dd
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# Datos de conexión a SQL Server
server = 'ec2-54-89-146-134.compute-1.amazonaws.com'
database = 'movielens'
username = 'SA'
password = 'YourStrong@Passw0rd'

# Construcción de la cadena de conexión y codificación segura de la URL
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn_str_quoted = urllib.parse.quote_plus(conn_str)

# Crear el engine con la cadena codificada
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str_quoted}")

# Leer datos de u.data (calificaciones) desde SQL Server
query_ratings = "SELECT user_id, item_id, rating, timestamp FROM u_data"
ratings_df = pd.read_sql(query_ratings, engine)

# Leer datos de u.user (información de usuarios)
query_users = "SELECT user_id, age, gender, occupation, zip_code FROM u_user"
users_df = pd.read_sql(query_users, engine)

# Leer datos de u.item (información de películas)
query_items = """
SELECT movie_id, movie_title, release_date, IMDb_URL, unknown, action, adventure, animation, 
[children's], comedy, crime, documentary, drama, fantasy, [film-noir], horror, musical, mystery, 
romance, [sci-fi], thriller, war, western 
FROM u_item
"""
items_df = pd.read_sql(query_items, engine)

# Convertir los DataFrames de Pandas a Dask DataFrames
ratings_dd = dd.from_pandas(ratings_df, npartitions=4)
users_dd = dd.from_pandas(users_df, npartitions=4)
items_dd = dd.from_pandas(items_df, npartitions=4)

# Unir los datasets: unir ratings con información de usuarios y películas
merged_dd = ratings_dd.merge(users_dd, on='user_id').merge(items_dd, left_on='item_id', right_on='movie_id')

# Ejemplo de procesamiento distribuido con Dask
# Calcular el promedio de calificaciones por género y edad
result = merged_dd.groupby(['age', 'action', 'comedy']).rating.mean().compute()

# Mostrar los resultados
print(result)
