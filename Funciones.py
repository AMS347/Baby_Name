import pandas as pd

def menu():
    print(chr(27) + "[0;33m" + """
    **********************************************************************************
    *  ****************************************************************************  *
    *  *                       NOMBRES POPULARES DE BEBE                          *  *
    *  *                                                                          *  *
    *  *   1. El top 10 de los nombres de bebés varones en un año.                *  *
    *  *   2. El top 10 de los nombres de bebés mujeres en un año.                *  *
    *  *   3. Los nombres de bebés varones en orden alfabético por año            *  *
    *  *   4. Los nombres de bebés mujeres en orden alfabético por año            *  *
    *  *   5. Estadística de los primeros 10 años de los nombres de bebés varones *  *
    *  *   6. Estadística de los primeros 10 años de los nombres de bebés mujeres *  *
    *  *   7. Acerca de…                                                         *  *
    *  *   8. Salir                                                               *  *
    *  ****************************************************************************  *
    **********************************************************************************
""")

    while True:  # Validar el ingreso
        try:
            op = int(input("Ingrese una opción: "))
            if op >= 1 and op <= 8:
                break
            else:
                print(chr(27) + "[0;31m" + "Número fuera del rango")

        except:
            print(chr(27) + "[0;31m" + "INGRESO NO VÁLIDO")

    print("\n")
    return op

def lecturaArchivo(año):
    nombre = "baby"+str(año)+".html"
    datos=[]

    try:
        archivo = open(nombre, "r+")
        lineas = archivo.readlines()
        for i in range(1000):
            temp = lineas[i+48].split("<td>")
            ranking=""
            hombre=""
            mujer=""
            for j in range(len(temp[1])):
                if temp[1][j]=="<":
                    break
                ranking += temp[1][j]
            for j in range(len(temp[2])):
                if temp[2][j]=="<":
                    break
                hombre += temp[2][j]
            for j in range(len(temp[3])):
                if temp[3][j]=="<":
                    break
                mujer+=temp[3][j]
            datos.append([año,ranking,hombre,mujer])
        archivo.close()  # Cierro el archivo
        return datos
    except:
        print("El año a consultar no existe!!!" + "\n")
        print(input(chr(27) + "[0;32m" + "Presione cualquier tecla para continuar"))
        return False

def top10Hombres(datos):
    print(("TOP 10 DE NOMBRES DE HOMBRES DEL AÑO "+ datos[0][0]).center(3,"-") + "\n")
    for i in range(10):
        print(datos[i][2])
    return()

def top10Mujeres(datos):
    print(("TOP 10 DE NOMBRES DE MUJERES DEL AÑO "+ datos[0][0]).center(3,"-") + "\n")
    for i in range(10):
        print(datos[i][3])
    return()

def hombresOrdenAlfabetico(datos):
    nombres=[]
    print(("NOMBRES DE HOMBRES DEL AÑO " + datos[0][0] + " EN ORDEN ALFABETICO").center(3, "-") + "\n")
    for i in range(len(datos)):
        nombres.append([datos[i][2],datos[i][1]])
    nombres.sort()
    for i in range(len(nombres)):
        print(nombres[i][0] + " " + nombres[i][1])
    return()

def mujeresOrdenAlfabetico(datos):
    nombres=[]
    print(("NOMBRES DE MUJERES DEL AÑO " + datos[0][0] + " EN ORDEN ALFABETICO").center(3, "-") + "\n")
    for i in range(len(datos)):
        nombres.append([datos[i][3],datos[i][1]])
    nombres.sort()
    for i in range(len(nombres)):
        print(nombres[i][0] + " " + nombres[i][1])
    return()

def estadisticaHombres():
    datosFinales=[]
    for i in range(0,12,2):
        datos=lecturaArchivo(str(1996+i))
        if 1996+i == 1996:
            for j in range(len(datos)):
                datosFinales.append([datos[j][2], datos[j][1], 0, 0, 0, 0, 0])
        elif 1996+i == 1998:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][2]==datosFinales[k][0]:
                        datosFinales[k][2]=datos[j][1]
                        flag=True
                if flag==False:
                    datosFinales.append([datos[j][2],0,datos[j][1],0,0,0,0])
        elif 1996+i == 2000:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][2]==datosFinales[k][0]:
                        datosFinales[k][3]=datos[j][1]
                        flag=True
                if flag==False:
                    datosFinales.append([datos[j][2],0,0,datos[j][1],0,0,0])
        elif 1996+i == 2002:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][2]==datosFinales[k][0]:
                        datosFinales[k][4]=datos[j][1]
                        flag=True
                if flag==False:
                    datosFinales.append([datos[j][2],0,0,0,datos[j][1],0,0])
        elif 1996 + i == 2004:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][2] == datosFinales[k][0]:
                        datosFinales[k][5] = datos[j][1]
                        flag = True
                if flag == False:
                    datosFinales.append([datos[j][2], 0, 0, 0,0, datos[j][1], 0])
        elif 1996 + i == 2006:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][2] == datosFinales[k][0]:
                        datosFinales[k][6] = datos[j][1]
                        flag = True
                if flag == False:
                    datosFinales.append([datos[j][2], 0, 0, 0,0, 0, datos[j][1]])
    datosFinales.sort()
    nombres = {"NAME": [], "1996": [], "1998": [], "2000": [], "2002": [], "2004": [], "2006": [], "PROMEDIO": []}
    indice = []
    for i in range(len(datosFinales)):
        prom = (int(datosFinales[i][1]) + int(datosFinales[i][2]) + int(datosFinales[i][3]) + int(
            datosFinales[i][4]) + int(datosFinales[i][5]) + int(datosFinales[i][6])) / 6
        nombres["NAME"].append(datosFinales[i][0])
        nombres["1996"].append(datosFinales[i][1])
        nombres["1998"].append(datosFinales[i][2])
        nombres["2000"].append(datosFinales[i][3])
        nombres["2002"].append(datosFinales[i][4])
        nombres["2004"].append(datosFinales[i][5])
        nombres["2006"].append(datosFinales[i][6])
        nombres["PROMEDIO"].append(str(prom))
        indice.append(i + 1)
    salida = pd.DataFrame(nombres, columns=["NAME", "1996", "1998", "2000", "2002", "2004", "2006", "PROMEDIO"],
                          index=indice)
    print(salida)
    return (datosFinales)

def estadisticaMujeres():
    datosFinales=[]
    for i in range(0,12,2):
        datos=lecturaArchivo(str(1996+i))
        if 1996+i == 1996:
            for j in range(len(datos)):
                datosFinales.append([datos[j][3], datos[j][1], 0, 0, 0, 0, 0])
        elif 1996+i == 1998:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][3]==datosFinales[k][0]:
                        datosFinales[k][2]=datos[j][1]
                        flag=True
                if flag==False:
                    datosFinales.append([datos[j][3],0,datos[j][1],0,0,0,0])
        elif 1996+i == 2000:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][3]==datosFinales[k][0]:
                        datosFinales[k][3]=datos[j][1]
                        flag=True
                if flag==False:
                    datosFinales.append([datos[j][3],0,0,datos[j][1],0,0,0])
        elif 1996+i == 2002:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][3]==datosFinales[k][0]:
                        datosFinales[k][4]=datos[j][1]
                        flag=True
                if flag==False:
                    datosFinales.append([datos[j][3],0,0,0,datos[j][1],0,0])
        elif 1996 + i == 2004:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][3] == datosFinales[k][0]:
                        datosFinales[k][5] = datos[j][1]
                        flag = True
                if flag == False:
                    datosFinales.append([datos[j][3], 0, 0, 0,0, datos[j][1], 0])
        elif 1996 + i == 2006:
            for j in range(len(datos)):
                flag = False
                for k in range(len(datosFinales)):
                    if datos[j][3] == datosFinales[k][0]:
                        datosFinales[k][6] = datos[j][1]
                        flag = True
                if flag == False:
                    datosFinales.append([datos[j][3], 0, 0, 0,0, 0, datos[j][1]])
    datosFinales.sort()
    nombres={"NAME":[],"1996":[],"1998":[],"2000":[],"2002":[],"2004":[],"2006":[],"PROMEDIO":[]}
    indice=[]
    for i in range(len(datosFinales)):
        prom = (int(datosFinales[i][1]) + int(datosFinales[i][2]) + int(datosFinales[i][3]) + int(
            datosFinales[i][4]) + int(datosFinales[i][5]) + int(datosFinales[i][6])) / 6
        nombres["NAME"].append(datosFinales[i][0])
        nombres["1996"].append(datosFinales[i][1])
        nombres["1998"].append(datosFinales[i][2])
        nombres["2000"].append(datosFinales[i][3])
        nombres["2002"].append(datosFinales[i][4])
        nombres["2004"].append(datosFinales[i][5])
        nombres["2006"].append(datosFinales[i][6])
        nombres["PROMEDIO"].append(str(prom))
        indice.append(i+1)
    salida=pd.DataFrame(nombres,columns=["NAME","1996","1998","2000","2002","2004","2006","PROMEDIO"],index=indice)
    print(salida)
    return(datosFinales)


def acerca():
    print("""
                        Autor:

        *Alex Mendoza

    """)
    return()

def cargarDatos(año,tipo):
    diccionario={}
    datos=lecturaArchivo(año)
    if tipo == "hombres":
        for i in range(len(datos)):
            diccionario[datos[i][2]]=datos[i][1]
    elif tipo == "mujeres":
        for i in range(len(datos)):
            diccionario[datos[i][3]]=datos[i][1]
    print(diccionario)
    return(diccionario)

