"""
Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
"""

alumnos = []

n = int(input("Cuántos alumnos tiene: "))

for i in range(n):
    nombre = input(f"Nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Calificación {j + 1} de {nombre}: "))
                if 0 <= nota <= 20:  
                    notas.append(nota)
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 20.")
            except ValueError:
                print("Error: Por favor ingrese un número válido para la calificación.")
    
    promedio = sum(notas) / len(notas) if notas else 0
    
    alumnos.append({"Alumno": nombre, "Notas": notas, "Promedio": promedio})

for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}, Promedio: {alumno['Promedio']:.2f}")
