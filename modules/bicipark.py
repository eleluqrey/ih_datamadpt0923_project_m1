#Librerías
import pandas as pd

#Este solo lee bicipark

#Función 1
#Defino una función que lea mi csv solución: csv que he generado desde el notebook con resultado data frame de todas las universidades junto a las estaciones de bicipark más cercanas.
def leer_solucion():
    return pd.read_csv("./data/solution/bicipark_solution.csv")


#Función 2
#Defino una función con dos entradas, el data frame anterior, y una user_selection. Voy a filtar por la universidad que el usuario elija, para devolverle directamente la distancia y la estación de bicipark más cercana a esa localización.
def filtro_solucion(df, user_selection):
    return df[df["title"] == user_selection][["address.street-address","distance"]]