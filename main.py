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
# FUNCIONES DE GESTIÓN DE PRODUCTOS
# ==========================================================

def registrar_producto():
    print("\nFuncionalidad en desarrollo.")


def mostrar_inventario():
    print("\nFuncionalidad en desarrollo.")


def buscar_producto():
    print("\nFuncionalidad en desarrollo.")


def actualizar_producto():
    print("\nFuncionalidad en desarrollo.")


def eliminar_producto():
    print("\nFuncionalidad en desarrollo.")


# ==========================================================
# FUNCIONES DE REPORTES
# ==========================================================

def mostrar_bajo_stock():
    print("\nFuncionalidad en desarrollo.")


def calcular_valor_total():
    print("\nFuncionalidad en desarrollo.")


def mostrar_estadisticas():
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
    print("6. Mostrar productos con bajo stock")
    print("7. Calcular valor total del inventario")
    print("8. Mostrar estadísticas")
    print("9. Salir")

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
            mostrar_bajo_stock()

        elif opcion == "7":
            calcular_valor_total()

        elif opcion == "8":
            mostrar_estadisticas()

        elif opcion == "9":
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