import os 

# LISTA PRINCIPAL: aquí guardo todos los usuarios, cada uno será un diccionario
usuarios = []

# FUNCIONES CRUD: cada operación tiene su propia función independiente

# CREAR: agrega un usuario nuevo a la lista
def agregar_usuario(rut, nombre, apellido, cargo, edad):
    # VALIDACIÓN DE DUPLICADOS: recorro la lista para verificar que el RUT no esté repetido
    for id in usuarios:
        if id["rut"] == rut:
            print("Error: Este RUT ya existe.")
            return   # Termina la función para evitar agregar un usuario duplicado
    # ESTRUCTURA DE DATOS: guardo los datos en un diccionario, edad es tipo INT obligatorio
    nuevo = {"rut": rut, "nombre": nombre, "apellido": apellido, "cargo": cargo, "edad": edad} #Diccionario =Clave y valor
    usuarios.append(nuevo)
    print(f"Usuario {nombre} {apellido} agregado correctamente.")

# LEER: muestra todos los usuarios guardados en la lista
def mostrar_usuarios():
    if len(usuarios) == 0:  #cuenta cuántos usuarios hay en la lista.
        print("No hay usuarios registrados.")
        return   # Termina la función para evitar que se siga ejecutando el resto del código
    print("\n--- DIRECTORIO DE USUARIOS ---")
    for nombres in usuarios:
       print(f"RUT: {nombres['rut']} | Nombre: {nombres['nombre']} {nombres['apellido']} | Cargo: {nombres['cargo']} | Edad: {nombres['edad']}")

# ACTUALIZAR: busca un usuario por RUT y modifica sus datos
def actualizar_usuario(rut, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_cargo):
    for n in usuarios:
        if n["rut"] == rut:
            n["nombre"] = nuevo_nombre
            n["apellido"] = nuevo_apellido
            n["cargo"] = nuevo_cargo
            n["edad"] = nueva_edad
            print(f"Usuario con RUT '{rut}' actualizado correctamente.")
            return # Termina la función después de actualizar el usuario
    print(f"No se encontró ningún usuario con el RUT '{rut}'.")

# ELIMINAR: busca un usuario por RUT y lo elimina de la lista
def eliminar_usuario(rut_buscar):
    for u in usuarios:
        if u["rut"] == rut_buscar:
            usuarios.remove(u)
            print(f"Usuario con RUT '{rut_buscar}' eliminado correctamente.")
            return  # Termina la función después de eliminar el usuario
    print(f"No se encontró ningún usuario con el RUT '{rut_buscar}'.")

# MENÚ INTERACTIVO: uso while True para que se repita hasta que el usuario elija salir
while True:
    os.system("cls")
    print("--- DIRECTORIO DE USUARIOS ---")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    print("------------------------------")
    opcion = input("Opción: ")

    if opcion == "1":
        os.system("cls")
        # VALIDACIONES: uso while True para que el usuario corrija el error al momento
        while True:
            rut = input("RUT: ")
            if "." in rut:
                print("Error: El RUT no debe tener puntos. Ejemplo: 12345678-9")
            elif "-" not in rut:
                print("Error: El RUT debe tener guión. Ejemplo: 12345678-9")
            else:
                break
        while True:
            nombre = input("Nombre: ")
            if nombre.strip() == "":
                print("Error: El nombre no puede estar vacío.")
            else:
                break
        while True:
            apellido = input("Apellido: ")
            if apellido.strip() == "":
                print("Error: El apellido no puede estar vacío.")
            else:
                break
        while True:
            cargo = input("Cargo: ")
            if cargo.strip() == "":
                print("Error: El cargo no puede estar vacío.")
            else:
                break
        while True:
            try:
                # EXCEPCIÓN: uso try/except para que no explote si escriben letras en vez de número
                edad = int(input("Edad: "))
                if edad < 18:
                    print("Error: El usuario debe ser mayor de edad (18+).")
                elif edad > 100:
                    print("Error: Ingresa una edad válida (máximo 100).")
                else:
                    break
            except ValueError:
                print("Error: La edad debe ser un número entero.")
        agregar_usuario(rut, nombre, apellido, cargo, edad)

    elif opcion == "2":
        os.system("cls")
        mostrar_usuarios()

    elif opcion == "3":
        os.system("cls")
        try:
            # EXCEPCIÓN: capturo el error si la edad ingresada no es un número
            rut = input("RUT del usuario a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            nueva_edad = int(input("Nueva edad: "))
            nuevo_cargo = input("Nuevo cargo: ")
            actualizar_usuario(rut, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_cargo)
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    elif opcion == "4":
        os.system("cls")
        rut = input("RUT del usuario a eliminar: ")
        eliminar_usuario(rut)

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")
    input("Presiona Enter para continuar...")