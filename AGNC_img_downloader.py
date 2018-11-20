import urllib.request
import glob, wget, csv, os

#Convierte archivo csv a texto

csv_file = input('Ingresa el nombre de tu archivo *.csv: ')
txt_file = input('Nombre del archivo *.txt de salida: ')
directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(", ".join(row)) for row in csv.reader(my_input_file, delimiter=' ', quotechar='|')]
    my_output_file.close()

# extraer el nombre del archivo de texto

txtnomb = glob.glob("%s" % (txt_file))
cadena = str(txtnomb)
encadenado = ''.join(cadena).replace('[\'','').replace('\']','').replace(' ','')

# convierte el texto en un array

mi_lista = open(encadenado, 'r')
mi_listado = mi_lista.read()
mi_cadena = mi_listado.split(",")

# guarda en la función "url_base" la dirección "estática" de cada elemento

url_base = "http://consulta.archivogeneral.gov.co/ConsultaWeb/assets/image?id={}"
repeticion = mi_cadena

rago = len(repeticion) -1

print("se están descargando %d imágenes" % (rago))
os.makedirs(directorio)
# loop para descargar las imágenes o mostrar un mensaje de error
for i in range(rago):
        try: 
                wget.download(url_base.format(repeticion[i]), "%s/%s.jpg" % (directorio, i))
        except:
                sys.exit("algo salió mal :(")

print("ha finalizado la descarga")
wait = input("Presione ENTER para salir.")
