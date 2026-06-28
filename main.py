# ==========================================================
# UNIVERSIDAD INTERNACIONAL DEL ECUADOR
# Carrera: Ingeniería en Desarrollo de Software
# Asignatura: Lógica de Programación
#
# Proyecto Final:
# Sistema de Control de Inventario para Tiendas
#
# Estudiante:
# María Sol León Molina
#
# Descripción:
# Sistema desarrollado en Python para administrar el
# inventario de una tienda mediante una aplicación de consola.
# ==========================================================


# ==========================================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================================

# En este proyecto no se requieren librerías externas.


# ==========================================================
# CONSTANTES
# ==========================================================

# Categorías disponibles para los productos.
# Se utiliza una tupla porque son datos constantes.

CATEGORIAS = (
    "Tecnología",
    "Oficina",
    "Hogar",
    "Limpieza",
    "Alimentos",
    "Bebidas"
)


# ==========================================================
# VARIABLES GLOBALES
# ==========================================================

# Lista que almacenará todos los productos del inventario.

inventario = []


# ==========================================================
# FUNCIONES DE UTILIDAD
# ==========================================================

def limpiar_pantalla():
    """Limpia visualmente la consola."""
    print("\n" * 50)


def pausar():
    """Pausa el programa hasta que el usuario presione Enter."""
    input("\nPresione ENTER para continuar...")

# ==========================================================
# FUNCIONES DE VALIDACIÓN
# ==========================================================

def validar_codigo():
    """Solicita un código y verifica que no esté repetido."""

    while True:

        codigo = input("Ingrese el código del producto: ").strip().upper()

        if codigo == "":
            print("El código no puede estar vacío.")
            continue

        repetido = False

        for producto in inventario:
            if producto["codigo"] == codigo:
                repetido = True
                break

        if repetido:
            print("Ese código ya existe. Intente con otro.")
        else:
            return codigo


def seleccionar_categoria():
    """Permite seleccionar una categoría mediante un número."""

    print("\nCategorías disponibles:")

    for indice, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{indice}. {categoria}")

    while True:

        opcion = input("\nSeleccione una categoría: ")

        if opcion.isdigit():

            opcion = int(opcion)

            if 1 <= opcion <= len(CATEGORIAS):
                return CATEGORIAS[opcion - 1]

        print("Opción inválida. Intente nuevamente.")


def leer_precio():
    """Solicita y valida el precio del producto."""

    while True:

        try:

            precio = float(input("Ingrese el precio: "))

            if precio > 0:
                return precio

            print("El precio debe ser mayor que cero.")

        except ValueError:
            print("Debe ingresar un valor numérico.")


def leer_stock():
    """Solicita y valida el stock del producto."""

    while True:

        try:

            stock = int(input("Ingrese el stock: "))

            if stock >= 0:
                return stock

            print("El stock no puede ser negativo.")

        except ValueError:
            print("Debe ingresar un número entero.")


# ==========================================================
# FUNCIONES DE GESTIÓN DE PRODUCTOS
# ==========================================================

def registrar_producto():
    """Registra un nuevo producto en el inventario."""

    limpiar_pantalla()

    print("=" * 55)
    print("               REGISTRAR PRODUCTO")
    print("=" * 55)

    codigo = validar_codigo()

    while True:

        nombre = input("Ingrese el nombre del producto: ").strip().title()

        if nombre == "":
            print("El nombre no puede estar vacío.")
        else:
            break

    categoria = seleccionar_categoria()

    precio = leer_precio()

    stock = leer_stock()

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    inventario.append(producto)

    print("\nProducto registrado correctamente.")


def mostrar_inventario():
    """Muestra todos los productos registrados."""

    limpiar_pantalla()

    print("=" * 55)
    print("             INVENTARIO DE PRODUCTOS")
    print("=" * 55)

    if len(inventario) == 0:
        print("\nNo existen productos registrados.")
        return

    for producto in inventario:

        print(f"Código     : {producto['codigo']}")
        print(f"Nombre     : {producto['nombre']}")
        print(f"Categoría  : {producto['categoria']}")
        print(f"Precio     : ${producto['precio']:.2f}")
        print(f"Stock      : {producto['stock']}")
        print("-" * 55)

    print(f"\nTotal de productos registrados: {len(inventario)}")

def buscar_producto():
    """Busca un producto por su código."""

    limpiar_pantalla()

    print("=" * 55)
    print("               BUSCAR PRODUCTO")
    print("=" * 55)

    if len(inventario) == 0:
        print("\nNo existen productos registrados.")
        return

    codigo = input("Ingrese el código del producto: ").strip().upper()

    for producto in inventario:

        if producto["codigo"] == codigo:

            print("\nProducto encontrado\n")

            print(f"Código     : {producto['codigo']}")
            print(f"Nombre     : {producto['nombre']}")
            print(f"Categoría  : {producto['categoria']}")
            print(f"Precio     : ${producto['precio']:.2f}")
            print(f"Stock      : {producto['stock']}")

            return

    print("\nNo se encontró ningún producto con ese código.")

def actualizar_producto():
    """Actualiza la información de un producto."""

    limpiar_pantalla()

    print("=" * 55)
    print("             ACTUALIZAR PRODUCTO")
    print("=" * 55)

    if len(inventario) == 0:
        print("\nNo existen productos registrados.")
        return

    codigo = input("Ingrese el código del producto a actualizar: ").strip().upper()

    for producto in inventario:

        if producto["codigo"] == codigo:

            print("\nProducto encontrado.\n")

            producto["nombre"] = input("Nuevo nombre: ").strip().title()

            print("\nCategorías disponibles:")

            for indice, categoria in enumerate(CATEGORIAS, start=1):
                print(f"{indice}. {categoria}")

            while True:

                opcion = input("\nSeleccione la nueva categoría: ")

                if opcion.isdigit():

                    opcion = int(opcion)

                    if 1 <= opcion <= len(CATEGORIAS):
                        producto["categoria"] = CATEGORIAS[opcion - 1]
                        break

                print("Opción inválida.")

            while True:

                try:

                    precio = float(input("Nuevo precio: "))

                    if precio > 0:
                        producto["precio"] = precio
                        break

                    print("El precio debe ser mayor que cero.")

                except ValueError:
                    print("Ingrese un número válido.")

            while True:

                try:

                    stock = int(input("Nuevo stock: "))

                    if stock >= 0:
                        producto["stock"] = stock
                        break

                    print("El stock no puede ser negativo.")

                except ValueError:
                    print("Ingrese un número entero.")

            print("\nProducto actualizado correctamente.")
            return

    print("\nNo se encontró el producto.")

def eliminar_producto():
    print("\nFuncionalidad en desarrollo.")

# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

def mostrar_menu():
    """Muestra el menú principal del sistema."""

    print("=" * 55)
    print("      SISTEMA DE CONTROL DE INVENTARIO")
    print("=" * 55)

    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

    print("=" * 55)


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    """Controla el flujo principal del programa."""

    while True:

        limpiar_pantalla()

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            actualizar_producto()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

        pausar()


# ==========================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================================

if __name__ == "__main__":
    main()