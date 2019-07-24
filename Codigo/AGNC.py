import urllib.request
import os, time

enlace = "http://consulta.archivogeneral.gov.co/ConsultaWeb/assets/image?id="
directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
init = input('Número de la imagen inicial: ')
fin = input('Número de la página final: ')

init_i = int(init)
fin_i = int(fin) + 1

lista = range(init_i,fin_i)

if not os.path.exists(directorio):
	os.makedirs(directorio)

print("Se van a descargar {} imágenes".format(fin_i-init_i))

for i in range(len(lista)):
        url = "{}{}".format(enlace, lista[i])
        print("descargando img {}".format(i+1))
        if not os.path.exists("{}/{}.jpg".format(directorio, i+1)):
                urllib.request.urlretrieve(url, "{}/{}.jpg".format(directorio, i+1))
                time.sleep(2)
        else:
                print("la imagen ya existe")
                pass
            

