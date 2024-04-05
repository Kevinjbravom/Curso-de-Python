from datetime import datetime 

tareas = []

def mostrar_tareas():
    
    def formatear_tarea(tarea):
        if tarea['status'] == 'pendiente'.lower():
            return f'Tarea pendiente: Código: {tarea["codigo"]} - Título: {tarea["titulo"]} - Descripción: {tarea["descripcion"]} - Fecha: {tarea["fecha"]}'
        elif tarea['status'] == 'completado'.lower():
            return f'Tarea completada: Código: {tarea["codigo"]} - Título: {tarea["titulo"]} - Descripción: {tarea["descripcion"]} - Fecha: {tarea["fecha"]}'
        else:
            return 'Tarea no guardada, error al ingresar el estado de la tarea'

    tareas_strings = list(map(formatear_tarea, tareas))
    
    for tarea_str in tareas_strings:
        print(tarea_str)

def agregar_tarea():
    while True:
        codigo = input('Ingrese el código de la tarea: ')
        if not codigo.isdigit():
            print('¡Error! El código debe ser numérico. Por favor, inténtelo de nuevo.')
            continue
        
        for tarea in tareas:
            if tarea['codigo'] == codigo:
                print('¡Error! El código de tarea ingresado ya está en uso.')
                return

        titulo = input('Ingrese el título de la tarea: ')
        descripcion = input('Ingrese la descripción de la tarea: ')
        status = input('Ingrese el estado de la tarea (completado o pendiente): ')
        fecha = input('Ingrese la fecha de la tarea (DD-MM-YYYY): ')

        nueva_tarea = {
            'codigo': codigo,
            'titulo': titulo,
            'descripcion': descripcion,
            'status': status,
            'fecha': fecha
        }
        tareas.append(nueva_tarea)
        print('Tarea agregada satisfactoriamente.')
        break

#FILTRAR TAREAS:

def filtrar_por_codigo():
    codigo_filtrar = input('Ingrese el código por el cual desea filtrar las tareas: ')
    tareas_filtradas = [tarea for tarea in tareas if tarea['codigo'] == codigo_filtrar]

    if not tareas_filtradas:
        print('No se encontraron tareas con ese código.')
    else:
        for tarea in tareas_filtradas:
            print("---------------")
            print(f"Código: {tarea['codigo']}")
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Estado: {'Completada' if tarea['status'] else 'pendiente'}")
            print(f"Fecha: {tarea['fecha']}")
            print('---------------')

def filtrar_por_titulo():
    titulo_filtrar = input('Ingrese el título por el cual desea filtrar las tareas: ')
    tareas_filtradas = [tarea for tarea in tareas if tarea['titulo'].lower() == titulo_filtrar.lower()]

    if not tareas_filtradas:
        print('No se encontraron tareas con ese título.')
    else:
        for tarea in tareas_filtradas:
            print("---------------")
            print(f"Código: {tarea['codigo']}")
            print(f"Título: {tarea['titulo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Estado: {'Completada' if tarea['status'] else 'pendiente'}")
            print(f"Fecha: {tarea['fecha']}")
            print("---------------")

    
def actualizar_tarea():
    
    codigo_actualizar = input('Ingrese el código de la tarea que desea actualizar: ')
    tarea_encontrada = False

    for tarea in tareas:
        if tarea['codigo'] == codigo_actualizar:
            print("")
            print('Tarea encontrada:')
            print("")
            print(f"Código: {tarea['codigo']} - Título: {tarea['titulo']} - Descripción: {tarea['descripcion']} - Fecha: {tarea['fecha']}")
            
            while True:
                print("")
                print("Sub-menú de Actualización:")
                print("1. Actualizar código (no se puede repetir con los códigos existentes)")
                print("2. Actualizar título")
                print("3. Actualizar descripción")
                print("4. Actualizar status (completado o pendiente)")
                print("5. Actualizar fecha")
                print("6. Atrás")
                print("")

                opcion = input("Seleccione una opción del menú: ")
                print("")

                if opcion == "1":
                    nuevo_codigo = input("Ingrese el nuevo código de la tarea: ")
                    if any(t['codigo'] == nuevo_codigo for t in tareas):
                        print("¡El código ingresado ya está en uso!")
                        print("")
                    else:
                        tarea['codigo'] = nuevo_codigo
                        print("Código actualizado correctamente.")
                        print("")

                elif opcion == "2":
                    nuevo_titulo = input("Ingrese el nuevo título de la tarea: ")
                    tarea['titulo'] = nuevo_titulo
                    print("Título actualizado correctamente.")
                    print("")

                elif opcion == "3":
                    nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
                    tarea['descripcion'] = nueva_descripcion
                    print("Descripción actualizada correctamente.")
                    print("")

                elif opcion == "4":
                    nuevo_status = input("Ingrese el nuevo estado de la tarea (completado o pendiente): ")
                    tarea['status'] = nuevo_status
                    print("Estado actualizado correctamente.")
                    print("")

                elif opcion == "5":
                    nueva_fecha = input("Ingrese la nueva fecha de la tarea (DD-MM-YYYY): ")
                    tarea['fecha'] = nueva_fecha
                    print("Fecha actualizada correctamente.")
                    print("")

                elif opcion == "6":
                    print("Volviendo al menú principal...")
                    print("")
                    break

                else:
                    print("Opción inválida. Por favor, seleccione una opción válida del menú.")
                    print("")

            tarea_encontrada = True
            break

    if not tarea_encontrada:
        print('No se encontró ninguna tarea con ese código.')
        print("")
        
def eliminar_tarea():
    codigo_eliminar = input('Ingrese el código de la tarea que desea eliminar: ')
    
    tareas_pendientes = list(filter(lambda tarea: tarea['codigo'] == codigo_eliminar and tarea['status'] == 'pendiente', tareas))
    tareas_completadas = list(filter(lambda tarea: tarea['codigo'] == codigo_eliminar and tarea['status'] == 'completado', tareas))
    if tareas_pendientes:
        tareas.remove(tareas_pendientes[0])
        print("")
        print('Tarea eliminada correctamente.')
        
    elif tareas_completadas:
        tareas.remove(tareas_completadas[0])
        print("")
        print('Tarea eliminada correctamente.')
        
    else:
        print("")
        print('No se encontró ninguna tarea pendiente con ese código.')
        
        

def main():
    while True:
        print("")
        print("Universidad Privada Dr.Rafael Belloso Chacín.")
        print("")
        print("|----------MENU DE TAREA----------|")
        print("|1- Lista de tarea.               |")
        print("|2- Filtrar tareas.               |")
        print("|3- Añadir tarea.                 |")
        print("|4- Actualizar tarea.             |")
        print("|5- Eliminar tarea.               |")
        print("|6- Salir del programa.           |")
        print("|---------------------------------|")
        print("")
        opcion = input("Elija un numero del menu: ")
        print("")
        
        if opcion == "1":
            subopcion = ''
            while subopcion != '3':
                print("")
                print("Sub-menú Lista de Tareas:")
                print("1. Completadas")
                print("2. Pendientes")
                print("3. Atrás")
                print("")
                subopcion = input("Ingrese el número de la opción: ")
                if subopcion == '1':
                    completadas = list(filter(lambda tarea: tarea['status'].lower() == 'completado', tareas))
                    print("Tareas Completadas:")
                    print("")
                    for tarea in completadas:
                        print(f"Código: {tarea['codigo']} - Título: {tarea['titulo']} - Descripción: {tarea['descripcion']} - Fecha: {tarea['fecha']}")
                elif subopcion == '2':
                    pendientes = list(filter(lambda tarea: tarea['status'].lower() == 'pendiente', tareas))
                    print("Tareas Pendientes:")
                    print("")
                    for tarea in pendientes:
                        print(f"Código: {tarea['codigo']} - Título: {tarea['titulo']} - Descripción: {tarea['descripcion']} - Fecha: {tarea['fecha']}")
            
        elif opcion == "2":
            print("Sub-menu Filtrar Tareas:")
            print("1-Filtrar por código")
            print("2-Filtrar por título")
            print("")
            filtro = input("Opción: ")

            if filtro == '1':
                filtrar_por_codigo()
            elif filtro == '2':
                filtrar_por_titulo()
            else:
                print("Opción inválida. Intente de nuevo.")
                print("")
            
            
        elif opcion == "3":
            print("Agregar tarea:")
            print("")
            agregar_tarea()
            print("")
            
        elif opcion == "4":
            print("")
            actualizar_tarea()
            print("")
            
        elif opcion == "5":
            print("Eliminar tarea:")
            eliminar_tarea()
            
        elif opcion == "6":
            print("Saliendo del programa...")
            print("")
            break
        else:
            print("Numero inválido. Por favor, seleccione un numero del menu válido.")
            print("")

if __name__ == "__main__":
    main()
   
   