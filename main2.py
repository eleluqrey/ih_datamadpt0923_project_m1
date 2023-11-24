from modules.hello_mod import * # solo es un ejempl
from modules import bicimad, bicipark
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()                    #Instancio el parser
    parser.add_argument("-us",type=str, help = "....")    #Añado argumentos
    parser.add_argument("-r",type=str, help = "Introduzca SI para mostrar resumen")     #Añado un argumento más
    parser.add_argument("-c",type=str, help = "Introduzca bicimad o bicipark")
    args = parser.parse_args()                            #Parseo argumentos

    if args.r == "SI":
        print("El usuario ha elegido mostrar el resumen: -------------")
        df_resumen = bicimad.leer_solucion()
        print("imprimo df ----------")
        print(df_resumen)

    elif args.c == "bicimad":
        df_resumen = bicimad.leer_solucion()
        print("imprimo -us:")
        print(args.us)

        df_filtered = bicimad.filtro_solucion(df_resumen,args.us)
        print(f"el user eligió: {args.us}...")

        print("EL BICIMAD MÁS CERCANO SE ENUENTRA EN.......")
        print(df_filtered)
        
    elif args.c == "bicipark":       
        df_resumen = bicipark.leer_solucion()
        print("imprimo -us:")
        print(args.us)

        df_filtered = bicipark.filtro_solucion(df_resumen,args.us)
        print(f"el user eligió: {args.us}...")

        print("EL BICIPARK MÁS CERCANO SE ENUENTRA EN.......")
        print(df_filtered) 