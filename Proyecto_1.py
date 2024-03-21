def listar_estudiantes(estudiantes):
    for estudiante in estudiantes:
        print("Nombre:", estudiante["nombre"])
        print("Apellido:", estudiante["apellido"])
        print("Cédula:", estudiante["cedula"])
        print("Nota 1:", estudiante["nota1"])
        print("Nota 2:", estudiante["nota2"])
        print("Nota 3:", estudiante["nota3"])
        print("Promedio", estudiante["promedio"])
        
        
        
        if estudiante["promedio"] <= 9.4:
             print(f"Estudiante: {estudiante["nombre"]} {estudiante["apellido"]}, Reprobado")
        else:
             print(f"Estudiante: {estudiante["nombre"]} {estudiante["apellido"]}, Aprobado")
    
        print("-------------------------")

def registrar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante universitario: ")
    apellido = input("Ingrese el apellido del estudiante universitario: ")
    cedula = input("Ingrese la cédula del estudiante universitario: ")
    nota1 = float(input("Ingrese la nota 1 del estudiante universitario: "))
    nota2 = float(input("Ingrese la nota 2 del estudiante universitario: "))
    nota3 = float(input("Ingrese la nota 3 del estudiante universitario: "))
    promedio = (nota1 + nota2 + nota3) / 3
    
    
    
    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "promedio": promedio,
    }
    estudiantes.append(estudiante)
    print("Estudiante universitario registrado exitosamente.")

def actualizar_estudiante(estudiantes, cedula_buscar):
    for estudiante in estudiantes:
        if estudiante["cedula"] == cedula_buscar:
            nota1 = float(input("Ingrese la nueva nota 1 del estudiante universitario: "))
            nota2 = float(input("Ingrese la nueva nota 2 del estudiante universitario: "))
            nota3 = float(input("Ingrese la nueva nota 3 del estudiante universitario: "))
            estudiante["nota1"] = nota1
            estudiante["nota2"] = nota2
            estudiante["nota3"] = nota3
            estudiante["promedio"] = (nota1 + nota2 + nota3) / 3
            print("Estudiante universitario actualizado exitosamente.")
            return
    print("Estudiante universitario no encontrado.")

def eliminar_estudiante(estudiantes, cedula_eliminar):
    for estudiante in estudiantes:
        if estudiante["cedula"] == cedula_eliminar:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado exitosamente.")
            return
    print("Estudiante universitario no encontrado")
    
# Menu principal
def main():
    estudiantes = []
    while True:
        print("")
        print("Universidad Privada Dr.Rafael Belloso Chacín.")
        print("")
        print("|------------MENU DEL USUARIO------------|")
        print("|1- Listado de estudiantes universitarios|")
        print("|2- Registrar estudiantes universitarios |")
        print("|3- Actualizar estudiantes universitarios|")
        print("|4- Eliminar estudiantes universitarios  |")
        print("|5- Salir del programa.                  |")
        print("|----------------------------------------|")
        print("")
        opcion = input("Elija un numero del menu: ")
        print("")
        if opcion == "1":
            print("Listado de estudiantes universitarios:")
            listar_estudiantes(estudiantes)
            print("")
        elif opcion == "2":
            registrar_estudiante(estudiantes)
            print("")
        elif opcion == "3":
            cedula_buscar = input("Ingrese la cédula del estudiante universitario a actualizar: ")
            actualizar_estudiante(estudiantes, cedula_buscar)
            print("")
        elif opcion == "4":
            cedula_eliminar = input("Ingrese la cédula del estudiante universitario a eliminar: ")
            eliminar_estudiante(estudiantes, cedula_eliminar)
            print("")
        elif opcion == "5":
            print("Saliendo del programa...")
            print("")
            break
        else:
            print("Numero inválido. Por favor, seleccione un numero del menu válido.")
            print("")

if __name__ == "__main__":
    main()
   