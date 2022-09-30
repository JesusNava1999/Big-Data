import json, csv

with open('C:/Users/elcor/OneDrive/Escritorio/UNIVERSIDAD/Big Data/Codes/subvenciones.json', encoding='utf-8') as fich_lect, open('C:/Users/elcor/OneDrive/Escritorio/UNIVERSIDAD/Big Data/Codes/subvenciones_agrupadas_con_gasto.json', 'w', encoding='utf-8') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)
    data = json.load(fich_lect)
    asoc_str: str = "Asociación"
    act_str = "Actividad Subvencionada"
    imp_str = "Importe en euros"
    lista = []
    lista_act = []
    asoc_actual = ""
    asoc = ""
    dicc = {}
    gasto = 0
    for elem in data:
        asoc = elem[asoc_str]
        act = elem[act_str]
        try:
            imp = float(elem[imp_str])
        except:
            for list in dict_lector:
                imp = float(list[imp_str])
        asoc_actual = asoc
        if asoc_actual != asoc:
            dicc["Actividades"] = lista_act
            dicc["Gasto"] = gasto
            dicc = {"Asociación": asoc}
            lista.append(dicc)
            lista_act = []
            gasto = 0
        print(asoc, act, imp)
        lista.append({act_str: act, imp_str: imp})
        gasto = gasto + imp
        asoc_actual = asoc
    print(lista)
    json.dump(lista, fich_escr, ensure_ascii=False, indent=4)  # , sort_keys=False

