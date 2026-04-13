# Ejemplo 1: Mensaje de saludo para la mañana
# Entrada: 9 AM
# Salida: "¡Buenos días!"

# Ejemplo 2: Mensaje de saludo para la tarde
# Entrada: 2 PM
# Salida: "¡Buenas tardes!"

# Ejemplo 3: Mensaje de saludo para la noche
# Entrada: 7 PM
# Salida: "¡Buenas noches!"

# Ahora, genera un código en python que tome la hora actual como entrada usando el módulo datetime
# y devuelva el mensaje de saludo apropiado

# Solución:
# Importar el módulo datetime

from datetime import datetime
def saludo_por_hora():
    # Obtener la hora actual
    hora_actual = datetime.now().hour

    # Determinar el mensaje de saludo basado en la hora
    if 5 <= hora_actual < 12:
        return "¡Buenos días!"
    elif 12 <= hora_actual < 18:
        return "¡Buenas tardes!"
    else:
        return "¡Buenas noches!"
# Ejemplo de uso
if __name__ == "__main__":
    mensaje_saludo = saludo_por_hora()
    print(mensaje_saludo)   
    

#suma de dos numeros





 