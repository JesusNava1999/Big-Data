import xlrd, xlwt, json

with xlrd.open_workbook('C:/Users/elcor/Desktop/UNIVERSIDAD/Big Data/Codes/XLS y Python/kardex grupal.xls') as libro, open('C:/Users/elcor/Desktop/UNIVERSIDAD/Big Data/Codes/XLS y Python/kardex_por_fecha.json', 'w', encoding='utf-8') as fich_k_mat:
    libro_escr = xlwt.Workbook(encoding='utf8', style_compression=0)
    hoja_escr = libro_escr.add_sheet('hoja1')
    fechas = []
    alumnos = []
    asings = []
    j_son = []

    materia={}
    materias=[]

    alumno={}
    alumnos=[]

    periodo={}

    index = 1;
    i = 1
    flag = False
    flag1 = False

    for hoja in libro.sheets():
        nRows = hoja.nrows
        fechas.append(str(hoja.row(1)[7].value))
        while(i<nRows):
            for el in fechas:
                if (el == hoja.row(i)[7].value):
                    flag = True
            if(flag):
                i = i + 1
                flag = False
            else:
                fechas.append(str(hoja.row(i)[7].value))
                index = index + 1
                i = i + 1
                flag = False
        #print(fechas)

        i = 1
        alumnos.append(str(hoja.row(1)[0].value))
        while (i < nRows):
            for al in alumnos:
                if (al == hoja.row(i)[0].value):
                    flag1 = True
            if (flag1):
                i = i + 1
                flag1 = False
            else:
                alumnos.append(str(hoja.row(i)[0].value))
                index = index + 1
                i = i + 1
                flag1 = False
        #print(alumnos)

        asings.append(str(hoja.row(1)[3].value))
        while (i < nRows):
            for el in asings:
                if (el == hoja.row(i)[3].value):
                    flag = True
            if (flag):
                i = i + 1
                flag = False
            else:
                asings.append(str(hoja.row(i)[3].value))
                index = index + 1
                i = i + 1
                flag = False

        for el in fechas:
            print(el)
            for al in alumnos:
                for i in range(1, nRows):
                    if (al==str(hoja.row(i)[0].value)):
                        if (el == str(hoja.row(i)[7].value)):
                            materia[str(hoja.row(i)[3].value)]=str(hoja.row(i)[5].value)
                            materias.append(materia)
                            materia={}
                if(materias):
                    print(al,materias)
                    alumno[al] = materias
                    materias=[]
                    alumnos.append(alumno)
                    alumno={}
                    periodo[el] = alumnos
            j_son.append(periodo)

    json.dump(j_son, fich_k_mat, ensure_ascii=False, indent=4)  # , sort_keys=False
