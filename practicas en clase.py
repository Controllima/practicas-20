trabajadores = []

"""Trabajador 1"""
nombre1 = input("Ingrese el nombre del primer trabajador: ")
edad1 = int(input("Ingrese la edad del primer trabajador: "))

print("Tipo de datos ingresados:")
print("Nombre 1:", type(nombre1))
print("Edad 1:", type(edad1))

trabajadores.append((nombre1, edad1))

"""Trabajador 2"""
nombre2 = input("Ingrese el nombre del segundo trabajador: ")
edad2 = int(input("Ingrese la edad del segundo trabajador: "))

print("Tipo de datos ingresados:")
print("Nombre 2:", type(nombre2))
print("Edad 2:", type(edad2))

trabajadores.append((nombre2, edad2))

"""Suma de las edades de los trabajadores"""
suma_edades = edad1 + edad2
print("La suma de las edades de los trabajadores es: {}".format(suma_edades))

"""Mostrar los trabajadores y sus edades"""
print("Trabajadores:")
for i, trabajador in enumerate(trabajadores):
    print("Trabajador", i + 1, "-", "Nombre:", trabajador[0], "Edad:", trabajador[1])
