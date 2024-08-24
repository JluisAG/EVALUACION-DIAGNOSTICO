
total_calf = 0
cont_aprob = 0
nombre_max = ""
nombre_min = ""
calificacion_max = -1
calificacion_min = 101

n = int(input("Ingresa el número de alumnos: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    suma_calificaciones = 0
    
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1} de {nombre} (0-100): "))
        suma_calificaciones += calificacion
    
    promedio_calificacion = suma_calificaciones / 3
    
    if promedio_calificacion <= 70:
        print(f"{nombre} está reprobado(a) con un promedio de {promedio_calificacion}.")
    else:
        total_calf += promedio_calificacion
        cont_aprob += 1

    if promedio_calificacion > calificacion_max:
        calificacion_max = promedio_calificacion
        nombre_max = nombre
    
    if promedio_calificacion < calificacion_min:
        calificacion_min = promedio_calificacion
        nombre_min = nombre

if cont_aprob > 0:
    promedio_aprob = total_calf / cont_aprob
    print(f"\nEl promedio de los alumnos aprobados es: {promedio_aprob:.2f}")

print(f"\nEl alumno con la calificación más alta es {nombre_max} con {calificacion_max}.")
print(f"El alumno con la calificación más baja es {nombre_min} con {calificacion_min}.")
