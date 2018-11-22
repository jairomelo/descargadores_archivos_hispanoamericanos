import requests, os, time

directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
ident = input('Número de la colección: ')
init = input('Número de la imágen inicial: ')
fin = input('Número de la página final: ')

url_entrada = 'http://pares.mcu.es/ParesBusquedas20/catalogo/show/{}'.format(ident)
url_imagen = 'http://pares.mcu.es/ParesBusquedas20/ViewImage.do?accion=42&txt_id_imagen=1&txt_rotar=0&txt_contraste=0&dbCode={}'

s = requests.Session()
# La primera petición obtiene las cookies [https://es.stackoverflow.com/a/215235/51760]
s.get(url_entrada)

os.makedirs(directorio)

init_i = int(init)
fin_i = int(fin)

lista = range(init_i,fin_i)

for i in range(len(lista)):
	url = url_imagen.format(lista[i])
	r = s.get(url)
	with open("%s/%s.jpg" % (directorio, i), 'wb') as handler:
		handler.write(r.content)
	time.sleep(3)
