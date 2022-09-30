import xlrd, xlwt, json

with xlrd.open_workbook('C:/Users/elcor/Desktop/UNIVERSIDAD/Big Data/Codes/XLS y Python/kardex grupal.xls') as libro, open('C:/Users/elcor/Desktop/UNIVERSIDAD/Big Data/Codes/XLS y Python/kardex_por_materias.json', 'w', encoding='utf-8') as fich_k_mat:
    libro_escr = xlwt.Workbook(encoding='utf8', style_compression=0)
    hoja_escr = libro_escr.add_sheet('hoja1')
    j_son = []
    materias = []
    calif = {}
    materia = {}
    asings = []
    index = 1;
    i = 1
    flag = False

    for hoja in libro.sheets():
        nRows = hoja.nrows
        asings.append(str(hoja.row(1)[3].value))
        while(i<nRows):
            for el in asings:
                if (el == hoja.row(i)[3].value):
                    flag = True
            if(flag):
                i = i + 1
                flag = False
            else:
                asings.append(str(hoja.row(i)[3].value))
                index = index + 1
                i = i + 1
                flag = False
        for el in asings:
            for i in range(1, nRows):
                if(el==str(hoja.row(i)[3].value)):
                    calif[str(hoja.row(i)[0].value)] = str(hoja.row(i)[5].value)
            materia[el] = calif
            materias.append(materia)
            calif = {}
            materia = {}
    j_son.append(materias)

    json.dump(j_son, fich_k_mat, ensure_ascii=False, indent=4)  # , sort_keys=False