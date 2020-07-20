from AGNMX import imagenes

'''
Para descargar el legajo solamente cambie la url por la que desee descargar.
'''

url = "https://archivos.gob.mx/guiageneral/visorimg/visorimg.php?CodR=MX09017AGNCL01FO001AYSE001APUI001"

try:
    imagenes(url)
except:
    raise
