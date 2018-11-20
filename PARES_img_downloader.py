import urllib.request
import re
import glob, wget, csv, os

print("Antes de utilizar este archivo, asegúrese que la carpeta desde la cual se ejecuta esté vacía de archivos *.jpg y *.txt")
wait = input("Presione ENTER para continuar.")

#Convierte archivo csv a texto

csv_file = input('Ingresa el nombre de tu archivo *.csv: ')
txt_file = input('Nombre del archivo *.txt de salida: ')
directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(", ".join(row)) for row in csv.reader(my_input_file, delimiter=' ', quotechar='|')]
    my_output_file.close()

# extraer el nombre del archivo de texto

txtnomb = glob.glob("*.txt")
cadena = str(txtnomb)
encadenado = ''.join(cadena).replace('[\'','').replace('\']','').replace(' ','')


# convierte el texto en un array

mi_lista = open(encadenado, 'r')
mi_listado = mi_lista.read()
mi_cadena = mi_listado.split(",")

#################

# guarda en la función "url_base" la dirección "estática" de cada elemento
url_base = "http://pares.mcu.es/ParesBusquedas20/ViewImage.do?accion=42&txt_id_imagen={}"
repeticion = mi_cadena

rago = len(repeticion) -1

print("se están descargando los archivos")
os.makedirs(directorio)
# loop para llamar cada página del repositorio y recolectar solo la información de los div que contengan la clase 'element-text'
for i in range(rago):
    url = url_base.format(repeticion[i])
    down = urllib.request.urlretrieve(url, "%s/%s.jpg" % (directorio, i))
