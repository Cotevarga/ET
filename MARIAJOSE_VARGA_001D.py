

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def validaNumEntero(mensaje:str):
    while True:
        try:
            opc = int(input(mensaje))
            if opc > 0:
                return opc
            else:
                print("DEBE INGRESAR UN NUMERO ENTERO POSITIVO")
                continue
        except ValueError :
            print("❌ DEBE INGRESAR UN NUMERO ENTERO POSITIVO")

def textoVacio(mensaje:str):
    while True:
        texto = input(mensaje)
        if len(texto) < 0:
            print("EL TEXTO NO DEBE ESTAR VACÍO")
        return texto
    
def stock_marca(mensaje:str):
    marca = textoVacio(mensaje).upper()
    for i in productos:
        if i[0][1].upper() == marca:
            print(f"El stock es {i[1]}")

def actualizar_precio(modelo,p):
    modelo = textoVacio("ingrese modelo a buscar")

def menu():
    while True:
        print(" *** MENÚ PRINCIPAL ***")
        print(" [1] - STOCK MARCA")
        print(" [2] - BUSQUEDA POR PRECIO")
        print(" [3] - ACTUALIZAR PRECIO")
        print(" [4] - SALIR")

        opc = validaNumEntero("INGRESE UNA OPCION 1 al 4: ")

        if opc == 1: 
         stock_marca()
            

        elif opc == 2: 
            print("2")

        elif opc == 3: 
            print("3")

        elif opc == 4: 
            print("PROGRAMA FINALIZADO")
            break

        else:
            print("❌ OPCION NO VÁLIDA")

menu()
