# Problema 5 - Horas semanales
# Fase 5 - Fundamentos de Programación

def calcular_total(horas):
    total = 0
    for h in horas:
        total = total + h
    return total

def clasificar_jornada(total):
    if total > 40:
        return "Sobretiempo"
    else:
        return "Horario estándar"

def main():
    matriz = [
        ["Ana Torres", 9, 8, 9, 8, 9],
        ["Luis Perez", 8, 8, 8, 8, 8],
        ["Maria Gomez", 7, 8, 7, 8, 7],
        ["Carlos Ruiz", 10, 9, 9, 8, 9]
    ]

    print("=== REPORTE DE HORAS SEMANALES ===")

    for fila in matriz:
        nombre = fila[0]
        horas = fila[1:6]
        total = calcular_total(horas)
        clasificacion = clasificar_jornada(total)

        print("Recurso:", nombre)
        print("Total horas:", total)
        print("Clasificación:", clasificacion)
        print("-------------------------")

main()
