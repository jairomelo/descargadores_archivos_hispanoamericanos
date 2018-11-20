import urllib.request
import wget

url_base = "http://hemeroteca.vanguardia.com/hemeroteca/public/periodico/img_pdf/vl/1953/1953-11-02/vl19531102%{}.jpg"
lista = "201,202,203,204,205,206,207,208,209"
repeticion = lista.split(",")

for i in range(0,8):
    url = url_base.format(repeticion[i])
    down = urllib.request.urlretrieve(url, "%s.jpg" % (i))