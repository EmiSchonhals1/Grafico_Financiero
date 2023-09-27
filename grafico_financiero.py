import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Función que permite al usuario crear y nombrar al archivo CSV
def crear_archivo() :
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    #definimos los campos que tendrá el DataFrame
    df = pd.DataFrame(columns = ["Fecha", "Gasto", "Ingreso", "Balance"])
    
    #while true: un bucle que continuará ejecutándose indefinidamente, a menos que se rompa explícitamente dentro del bucle o se detenga el programa de alguna otra manera, en este caso se detiene con un break si el usuario no desea continuar con la carga de datos
    while True:
        fecha = input("Ingrese la fecha en formato DD/MM/AA: ")
        gasto = float(input(f"Ingrese el gasto del día {fecha}: "))
        ingreso = float(input(f"Ingrese el ingreso del día {fecha}: "))
        balance = ingreso - gasto
        
        #agregamos los datos al DataFrame
        nuevo_registro = pd.DataFrame({"Fecha": [fecha], "Gasto": [gasto], "Ingreso": [ingreso], "Balance": [balance]})
        df = pd.concat([df, nuevo_registro], ignore_index=True)
        #el parámetro ignore_index=True hace que pandas ignore los índices existentes en los objetos que estamos concatenando y crea un nuevo índice numérico para el resultado concatenado.
        
        
        #preguntamos al usuario si desea seguir agregando datos
        continuar = input("¿Desea agregar algún dato? S/N: ").strip().upper()
        #si el usuario no ingreso la opción S se cierra el bucle infinito del while true :
        if continuar != "S" :
            break
        
        
    
    #guardamos el DataFrame en un archivo CSV
    df.to_csv(f"{nombre_archivo}.csv", index=False)
    print(f"Archivo {nombre_archivo} creado correctamente")
    
    
    
#Función que genera el gráfico
def generar_grafico() :
    nombre_archivo = input("Ingrese el nombre del archivo a analizar: ")
    
    #si el archivo existe se guarda como CSV, sino se ejecuta el except y se pide el reingreso del nombre
    try: 
        df = pd.read_csv(f"{nombre_archivo}.csv")
    except FileNotFoundError :
        print(f"El archivo {nombre_archivo}.csv no existe")
        return  #si el archivo no existe se vuelve al inicio de la función para el nuevo ingreso del nombre del mismo
    
    
    #creamos el gráfico de barras
    plt.figure(figsize=(10, 6))
    #depende del valor del balance será el color del gráfico
    colores = ["red" if balance < 0 else "green" if balance > 0 else "blue" for balance in df["Balance"]]
    plt.bar(df["Fecha"], df["Balance"], label="Balance", color=colores)
    plt.xlabel("Fecha") #el eje X será Fecha
    plt.ylabel("Balance") #el eje Y será Balance
    plt.title("Balances Diarios") #título del gráfico
    plt.legend()
    plt.xticks(rotation=45)#los nombres del eje X tendrán una rotación de 45
    
    #mostramos el gráfico
    plt.tight_layout()
    plt.show()
    
    
    
#por último, creamos el menú principal
#utilizamos el bucle infinito while true :, el mismo se cortará usando un break si el usuario elige salir del programa con la opción 3
while True :
    print("\nMenú Principal")
    print("1: Crear un nuevo archivo")
    print("2: Generar un gráfico de gastos e ingresos")
    print("3: Salir")
    
    opcion = input("Seleccione una opción: ")
    if opcion == "1" :
        crear_archivo()
    elif opcion == "2" :
        generar_grafico()
    elif opcion == "3" :
        break
    else :
        print("Opción inválida, por favor ingrese una opción válida...")