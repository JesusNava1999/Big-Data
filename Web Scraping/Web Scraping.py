import requests, csv
import matplotlib.pyplot as plt
url1 = 'http://www.mambiente.munimadrid.es/opendata/horario.txt'
url2 = 'https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html'
resp = requests.get(url1)
print(resp)

with open('C:/Users/elcor/Desktop/UNIVERSIDAD/Big Data/Codes/Web Scraping/horario.txt','wb') as output: output.write(resp.content)
with open('C:/Users/elcor/Desktop/UNIVERSIDAD/Big Data/Codes/Web Scraping/horario.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] + row[1] == '28079' and row[3] == '01':
            plt.title("Oxido de nitrogeno: " + row[8] + "/" + row[7] + "/" + row[6])
        hora = 0
        desp = 9
        vs = []
        horas = []
        while hora <= 23:
            if row[desp + 2 * hora + 1] == 'V':
                vs.append(row[desp + 2 * hora])
                horas.append(hora)
            hora += 1
plt.plot(horas, vs)
plt.show()

# 0, 1, 2
# 3, 4, 5
# --- col 3 = 12 -> Media Nitrogeno
# 6, 7, 8 -> año, mes, dia
# 9-56 hora del dia
# medicion V = valido, N = no considerar

# https://semadet.jalisco.gob.mx/medio-ambiente/calidad-del-aire?sm_search_api_multi_aggregation_1=Secretar%C3%ADa%20de%20Medio%20Ambiente%20y%20Desarrollo%20Territorial%20OR%20%2AGobierno%2Adel%2AEstado%2Ade%2AJalisco&page=1