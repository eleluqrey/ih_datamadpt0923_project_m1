# 1º. Importar

#Importo bicipark y bicimad .py , también importo argparse que vamos a usarlo para construir mi interacción con el usuario
from modules import bicimad, bicipark
import argparse

# 2º. Método argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()                                                   #Instancio el parser

    #Añadimos argumentos, cada argumento en una línea:
    parser.add_argument("-c",type=str, help = "Introduzca bicimad o bicipark")           #Añado primer argumento: ¿Bicimad o bicipark?
    parser.add_argument("-r",type=str, help = "Introduzca SI para mostrar resumen")      #Añado segundo argumento: ¿Resumen de todas las universidades junto a estaciones de bicimad/bicipark más cercanas?
    parser.add_argument("-us",type=str, help = "Introduzca universidad")                 #Añado tercer argumento: ¿Filtrar por una universidad?

    args = parser.parse_args()                                                           #Parseo argumentos

  
# 3º. 

# Paso 1. En el primer argumento, nuestra primera condición es que el usuario elija entre bicimad o bicipark

# Si es bicimad:
    if args.c == "bicimad":
        df_resumen = bicimad.leer_solucion()
#       print("imprimo -us:")

#        Paso 2. En el segundo argumento, queremos saber si el usuario quiere un resumen completo o filtar por la localización en la que se encuentre

#        Si la respuesta es SI quiere resumen:

        if args.r == "SI":
#         print("El usuario ha elegido mostrar el resumen: -------------")
          print("Aquí tienes el resumen de universidades y estaciones de bicimad cercanas: ")
          df_resumen = bicimad.leer_solucion()
#         print("imprimo df ----------")
          print(df_resumen)

#        Si la respuesta no es SI, tiene que introducir el siguiente argumento que es la universidad por la que quiere filtrar:

        else:
          df_filtered = bicimad.filtro_solucion(df_resumen,args.us)
          print(f"Has elegido la localización: {args.us} ")
          print("Te mostramos la estación de bicimad más cercana :")
          print(df_filtered) 

# Si es bicipark:      
        
    elif args.c == "bicipark":       
        df_resumen = bicipark.leer_solucion()
#       print("imprimo -us:")
#       print(args.us)
        
#       Si la respuesta es SI quiere resumen:

        if args.r == "SI":
#         print("El usuario ha elegido mostrar el resumen: ------------")
          print("Aquí tienes el resumen de universidades y estaciones de bicipark cercanas: ")
          df_resumen = bicipark.leer_solucion()
#         print("imprimo df ----------")
          print(df_resumen)

#       Si la respuesta no es SI, tiene que introducir el siguiente argumento que es la universidad por la que quiere filtrar:

        else:
            df_filtered2 = bicipark.filtro_solucion(df_resumen, args.us)
            print(f"Has elegido la localización: {args.us} ")

            print("Te mostramos la estación de bicipark más cercana :")

            print(df_filtered2) 