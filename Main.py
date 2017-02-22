from Funciones import *

while True:
    op = menu()
    if op==1:
        año=str(input("Ingrese el año que desea consultar los nombres:"))
        while True:
            if lecturaArchivo(año)!=False:
                top10Hombres(lecturaArchivo(año))
            op2=str(input("Desea consultar otro año (si o no)?"))
            if op2.upper()=="SI":
                año=str(input("Ingrese otro año:"))
                continue
            else:
                break
        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")

    elif op==2:
        año = str(input("Ingrese el año que desea consultar los nombres:"))
        while True:
            if lecturaArchivo(año)!=False:
                top10Mujeres(lecturaArchivo(año))
            op2=str(input("Desea consultar otro año (si o no)?"))
            if op2.upper()=="SI":
                año=str(input("Ingrese otro año:"))
                continue
            else:
                break
        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")

    elif op==3:
        año = str(input("Ingrese el año que desea consultar los nombres:"))
        while True:
            if lecturaArchivo(año)!=False:
                hombresOrdenAlfabetico(lecturaArchivo(año))
            op2=str(input("Desea consultar otro año (si o no)?"))
            if op2.upper()=="SI":
                año=str(input("Ingrese otro año:"))
                continue
            else:
                break
        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")

    elif op==4:
        año = str(input("Ingrese el año que desea consultar los nombres:"))
        while True:
            if lecturaArchivo(año)!=False:
                mujeresOrdenAlfabetico(lecturaArchivo(año))
            op2=str(input("Desea consultar otro año (si o no)?"))
            if op2.upper()=="SI":
                año=str(input("Ingrese otro año:"))
                continue
            else:
                break
        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")

    elif op==5:
        datosFinales=estadisticaHombres()
        while True:
            nombre = str(input("Buscar nombre de bebé, ingrese el nombre a buscar:"))

            for i in range(len(datosFinales)):
                if (datosFinales[i][0].upper()) == (nombre.upper()):
                    print("Estadística de " + nombre.upper() + ":")
                    print(datosFinales[i][0] + "\t" + "\t" + "\t" + str(datosFinales[i][1]) + "\t" + "\t" + str(
                        datosFinales[i][2]) + "\t" + "\t" + str(datosFinales[i][3]) + "\t" + "\t" + str(
                        datosFinales[i][4]) + "\t" + "\t" + str(datosFinales[i][5]) + "\t" + "\t" + str(
                        datosFinales[i][6]))

            op2=(str(input("Desea Buscar otro nombre (si o no)?")))
            if op2.upper()=="SI":
                continue
            else:
                break

        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")

    elif op==6:
        datosFinales = estadisticaMujeres()
        while True:
            nombre = str(input("Buscar nombre de bebé, ingrese el nombre a buscar:"))

            for i in range(len(datosFinales)):
                if (datosFinales[i][0].upper()) == (nombre.upper()):
                    print("Estadística de " + nombre.upper() + ":")
                    print(datosFinales[i][0] + "\t" + "\t" + "\t" + str(datosFinales[i][1]) + "\t" + "\t" + str(
                        datosFinales[i][2]) + "\t" + "\t" + str(datosFinales[i][3]) + "\t" + "\t" + str(
                        datosFinales[i][4]) + "\t" + "\t" + str(datosFinales[i][5]) + "\t" + "\t" + str(
                        datosFinales[i][6]))

            op2 = (str(input("Desea Buscar otro nombre (si o no)?")))
            if op2.upper() == "SI":
                continue
            else:
                break

        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")
    elif op==7:
        acerca()
        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        print("\n")

    elif op==8:
        break
