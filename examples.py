# Archivo para probar los métodos de la librería

# Importamos los métodos definidos en los módulos lineal e iterativos
from DM23004UNO.lineal import (
    gauss_elimination, gauss_jordan, cramer, lu_decomposition
)
from DM23004UNO.iterativos import jacobi, gauss_seidel
from DM23004UNO.no_lineal import biseccion

# Función de utilidad para imprimir soluciones de manera formateada
def imprimir_solucion(metodo, solucion):
    print(f"Solución por {metodo}:")
    for i, valor in enumerate(solucion, 1):
        print(f"  x{i} = {valor:.4f}")
    print("-" * 40)

# Función para mejorar la impresión del método de Bisección
def imprimir_biseccion(a, b, raiz, iteraciones, tol):
    print("\n" + "="*40)
    print(f"Método de Bisección: Encontrar la raíz de f(x) en el intervalo [{a}, {b}]")
    print(f"Raíz aproximada: {raiz:.10f}")
    print(f"Intervalo final: [{a}, {b}]")
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Tolerancia utilizada: {tol}")
    print("="*40)

# Punto de entrada del script
if __name__ == "__main__":
    # -----------------------------
    # 1. Eliminación de Gauss
    # -----------------------------
    # Sistema de ecuaciones: 3x3
    A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b1 = [8, -11, -3]
    # Se realiza una copia profunda para evitar modificar las matrices originales
    imprimir_solucion("Eliminación de Gauss", gauss_elimination([row[:] for row in A1], b1[:]))

    # -----------------------------
    # 2. Gauss-Jordan
    # -----------------------------
    A2 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b2 = [8, -11, -3]
    imprimir_solucion("Gauss-Jordan", gauss_jordan([row[:] for row in A2], b2[:]))

    # -----------------------------
    # 3. Regla de Cramer
    # -----------------------------
    A3 = [[2, -1, 5], [3, 2, 2], [1, 3, 3]]
    b3 = [-3, 12, 7]
    imprimir_solucion("Regla de Cramer", cramer([row[:] for row in A3], b3[:]))

    # -----------------------------
    # 4. Descomposición LU
    # -----------------------------
    A4 = [[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]
    b4 = [-2, 9, -5]
    imprimir_solucion("Descomposición LU", lu_decomposition([row[:] for row in A4], b4[:]))

    # -----------------------------
    # 5. Método de Jacobi
    # -----------------------------
    # Sistema de 4 ecuaciones. La matriz A debe ser diagonalmente dominante
    A5 = [[10, -1, 2, 0],
          [-1, 11, -1, 3],
          [2, -1, 10, -1],
          [0, 3, -1, 8]]
    b5 = [6, 25, -11, 15]
    imprimir_solucion("Método de Jacobi", jacobi([row[:] for row in A5], b5[:]))

    # -----------------------------
    # 6. Método de Gauss-Seidel
    # -----------------------------
    # Se usa el mismo sistema que Jacobi para comparar resultados
    A6 = [[10, -1, 2, 0],
          [-1, 11, -1, 3],
          [2, -1, 10, -1],
          [0, 3, -1, 8]]
    b6 = [6, 25, -11, 15]
    imprimir_solucion("Método de Gauss-Seidel", gauss_seidel([row[:] for row in A6], b6[:]))
    
    # -----------------------------
    # 7. Método de Bisección
    # -----------------------------
    # Definimos una función no lineal, por ejemplo: f(x) = x^2 - 2 (raíz en x = sqrt(2))
    def f(x):
        return x**2 - 2

    # Usamos el método de Bisección para encontrar la raíz de f(x) en el intervalo [1, 2]
    raiz = biseccion(f, 1, 2)
    
    # Mejoramos la impresión para el Método de Bisección
    imprimir_biseccion(1, 2, raiz, 100, 1e-10)
