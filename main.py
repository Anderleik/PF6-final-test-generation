import json
import requests

def dish_fetch(num):
    #Función que recibe un número (ID) y retorna un diccionario con la info del plato.
    try:
        #Para el manejo de errores, convertimos el input a int y si falla, retornamos un error.
        num_id = int(num)
    except ValueError:
        return {"error": "Entrada inválida. Por favor ingresa un número."}
        
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num_id}")
    # Configuramos la API.
    if response.status_code == 200:
    # Esta condicion me permite hacer una verificación de que la conexion con la API fue exitosa (código 200).
        return json.loads(response.content)
    else:
    #Si no es exitosa la conexión, retornara un mensaje de error.
        return {"error": f"No se encontró el plato con ID {num_id}."}

def mostrar_directorio():
    # Función que me ayuda a mostrar los platos con su respectivo codigo.
    print("\nCargando el directorio de platos disponibles...")
    response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
    
    if response.status_code == 200:
        platos = json.loads(response.content)
        print("\n" + "="*40)
        print("   CÓDIGOS DE PLATOS TÍPICOS")
        print("="*40)
        # Recorremos la lista y mostramos el ID junto al nombre
        for plato in platos:
            print(f"ID: {plato['id']:<3} | {plato['name']}")
        print("="*40)
    else:
        print("No se pudo cargar el directorio.")

def main():
    print("¡Hola, estudiantes! Bienvenidos al menú interactivo.")
    
    # 1. Le mostramos los códigos al usuario
    mostrar_directorio()
    
    # 2. Iniciamos el ciclo interactivo
    while True:
        print("\n(Escribe '0' para salir del programa)")
        # Despues de ver la lista, ahora ya sabemos qué número poner
        seleccion = input("Ingresa el ID (número) del plato que deseas consultar: ")
        
        if seleccion == '0':
            print("Saliendo del programa. ¡Buen provecho!")
            break
            
        # 3. Usamos la funcion solicitada (dish_fetch) para obtener la información del plato
        resultado = dish_fetch(seleccion)
        
        # 4. Mostramos el resultado.
        print("\n--- Resultado de la búsqueda ---")
        if "error" in resultado:
            print(f"{resultado['error']}")
        else:
            print(f"Plato: {resultado['name']}")
            print(f"Descripción: {resultado['description']}")

if __name__ == "__main__":
    main()