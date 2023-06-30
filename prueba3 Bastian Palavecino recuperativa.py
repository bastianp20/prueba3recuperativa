datos = []
buscar = []
lista_personas = [datos,1,2]
def datos_personales(): 
    while True: 
        try:    
            nombre = input("ingrese su nombre: ")
            if len(nombre) < 8: 
                print("tu nombre es inferior a 8 caracteres ")
                break
            elif len(nombre) > 8: 
                print("rango de caracteres correctos¡")
            nif = int(input("ingrese su rut: "))
            dv_nif = input("ingrese su digito verificador: ").upper()
            if len(dv_nif) < 1: 
                print("su digito verificador es incorrecto ")
                print("usted no pertenece a la union europea")
                break
            elif len(dv_nif) == 3: 
                print("digito verificador admitido")
                print("usted pertenece a la union europea")
            edad = int(input("ingrese su edad: "))
            if edad < 0: 
                print("tu edad no puede ser menor a 0")
            elif edad > 0: 
                print("rango de edad correcto¡ ")
            datitos = [nombre,edad, nif, dv_nif]
            datos.append(datitos)
            print(datos)
            break
        except: 
            print("ingresa tus datos nuevamente")
        

def buscar_persona():
    nombre = input("ingrese su nombre: ")
    for persona in datos: 
        print(datos)
        if persona[0] == nombre: 
            datos_buscados = str(persona[2]) + '-' + persona[3]
            certificado_generado = 'nombre: ' + str(persona[0]) + ', edad: ' + str(persona[1]) + ', rut: ' + str(persona[2]) + ', dv: ' + str(persona[3]) 
            print(datos_buscados)
            print("persona encontrada")
            print("y su certificado es el siguiente: ")
            print(certificado_generado)


while True:  

    print("[1]    datos personales ")
    print("[2]   buscar persona y generar certificado  ")
    print("[3]    salir de la opcion   ")
    menu = int(input("ingrese una opcion: "))
    if menu == 1: 
        datos_personales()
    elif menu == 2: 
        buscar_persona()
    elif menu == 3: 
        break

