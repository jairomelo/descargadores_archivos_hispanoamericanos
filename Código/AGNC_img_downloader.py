import urllib.request
import os, time

enlace = "http://consulta.archivogeneral.gov.co/ConsultaWeb/assets/image?id="
directorio = "SC_NE_CUND_l.34.2" #input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
init = "1002079" #input('Número de la imagen inicial: ')
fin = "1002084" #input('Número de la página final: ')

init_i = int(init)
fin_i = int(fin) + 1

lista = range(init_i,fin_i)

if not os.path.exists(directorio):
	os.makedirs(directorio)

for i in range(len(lista)):
    url = "{}{}".format(enlace, lista[i])
    #TRY urlretrieve url -> error 500 -> pass
    urllib.request.urlretrieve(url, "{}/{}.jpg".format(directorio, i))
    time.sleep(2)

