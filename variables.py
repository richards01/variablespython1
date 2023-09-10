# Definir una variable de cada tipo de primitivo
cadena = "Hola, soy richard tengo 23 años"
entero = 42
flotante = 3.1416

# Concatenar la cadena con las otras variables
resultado_concatenacion = cadena + " - Entero: " + str(entero) + " - Flotante: " + str(flotante)

# Imprimir la cadena resultante
print("Resultado de la concatenación:")
print(resultado_concatenacion)

# Límites de los enteros y los flotantes en Python
# - Los enteros en Python no tienen un límite fijo, pueden ser tan grandes como la memoria del sistema lo permita.
# - Los flotantes en Python siguen el estándar IEEE 754 y tienen límites definidos por la precisión de la máquina.
#   El valor máximo positivo de un flotante de doble precisión es aproximadamente 1.8 x 10^308.

# Calcular la suma de los primeros n números pares
n = 5  # Puedes cambiar el valor de n según tus necesidades
suma_pares = n * (n + 1)

# Imprimir el resultado de la suma
print("\nResultado de la suma de los primeros", n, "números pares:")
print(suma_pares)
