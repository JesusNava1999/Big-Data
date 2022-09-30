# Nava Cuellar José De Jesús
# No. Control: 18011108
# Big Data

import xlrd, xlwt

with xlrd.open_workbook('C:/Users/elcor/OneDrive/Escritorio/UNIVERSIDAD/Big Data/Codes/XLS y Python/kardex.xls') as libro:
    asocs = {}  # Crear diccionario vacio
    libro_escr = xlwt.Workbook(encoding='utf8', style_compression=0) # Leer el archivo completo
    hoja_escr = libro_escr.add_sheet('Hoja1') # Leer una sola hola
    hoja_escr.write(0, 0, 'CAL') # Escribir una columna
    hoja_escr.write(0, 1, 'Entrenamiento') # Escribir una columna
    for hoja in libro.sheets(): #Loop de hojas
        asocs = hoja.row(0) # Iguala el diccionario a la primer fila
        nCol = hoja.nrows # Iguala el numero de filas
        sum = prom80 = prom70 = sum80 = sum70 = 0 # Declaración de Variables
        for i in range(1, nCol): # Loop de filas
            fila = hoja.row(i) # Extrae la fila
            calificacion = float(fila[4].value) # Convierte los valores de la fila a float y lo asigna a calificación
            hoja_escr.write(i, 0, calificacion) # Escribe en el nuevo archivo en la fila i y la columna 0
            if calificacion == 70:              # Conficionales
                hoja_escr.write(i, 1, "SI")
            else:
                hoja_escr.write(i, 1, "NO")
            if calificacion >= 80:
                prom80 += calificacion
                sum80 += 1
            if 70 <= calificacion < 80:
                prom70 += calificacion
                sum70 += 1
            sum += calificacion
        print('Promedio general: ' + str(sum / (nCol - 1))) # Imprime el promedio
        if sum80:
            print('Promedio mayor a 80: ' + str(prom80 / sum80))
        if sum70:
            print('Promedio menor a 70: ' + str(prom70 / sum70))  # Guarda todo en el archivo del path
    libro_escr.save('C:/Users/elcor/OneDrive/Escritorio/UNIVERSIDAD/Big Data/Codes/XLS y Python/kardex-nuevo.xls')
