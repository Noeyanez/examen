prod = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stockmarca(marca):
    total=0
    for modelo in prod:
        if prod[modelo][0].lower() == marca.lower():
            if modelo in stock:
                total += stock[modelo][1]
    print(f"\nel stock es: {total}")

def buscarprecio(pmin, pmax):
    resultado = []
    for modelo in stock:
        precio, cantidad = stock[modelo]
        if pmin <= precio <= pmax and cantidad > 0:
            if modelo in prod:
                marca = prod[modelo][0]
                resultado.append(f"{marca}--{modelo}")
    if resultado:
        resultado.sort()
        print("\nlos notebooks entre los precios consultados son:", resultado)
    else:
        print("\nno hay notebooks en ese rango de precios.")

def actprecio(modelo, nprecio):
    if modelo in stock:
        stock[modelo][0] = nprecio
        return True
    else:
        return False

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. stock marca")
        print("2. busqueda por precio")
        print("3. actualizar precio")
        print("4. salir")

        opcion = input("ingrese una opcion: ")

        if opcion == '1':
            marca = input("ingrese marca a consultar: ")
            stockmarca(marca)

        elif opcion == '2':
            while True:
                try:
                    pmin = int(input("ingrese precio minimo: "))
                    pmax = int(input("ingrese precio max: "))
                    break
                except ValueError:
                    print("\ndbe ingresar valores enteros")
            buscarprecio(pmin, pmax)

        elif opcion == '3':
            while True:
                modelo = input("ingrese modelo a actualizar: ")
                try:
                    nprecio = int(input("ingrese precio nuevo: "))
                except ValueError:
                    print("\ndebe ingresar un precio valido.")
                    continue

                if actprecio(modelo, nprecio):
                    print("\nprecio actualizado")
                else:
                    print("\nel modelo no existe")

                continuar = input("desea actualizar otro precio (si/no)?: ").lower()
                if continuar != 'si':
                    break

        elif opcion == '4':
            print("\nprograma finalizado...")
            break

        else:
            print("\ndebe seleccionar una opcion valida")

menu()