---
layout: page
title: Descargar múltiples imágenes desde PARES.
permalink: /tutoriales/ayuda/PARES_img_downloader
---

En este pequeño tutorial quisiera mostrar cómo utilizar el programa `PARES_img_downloader.py`

## Requisitos

* [Python 3](https://www.python.org/)
* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)
* [Selenium 3](https://pypi.org/project/selenium/)
* [Chromedriver](http://chromedriver.chromium.org/downloads)

Para poder utilizar este programa es indispensable tener instalado [Python 3](https://www.python.org/). Usuarios de Linux y Mac ya deberían tener instalado Python.
Para saber si la versión de Python es adecuada, ejecutar el siguiente comando desde la terminal:

```Linux y Mac
$ python --version
```

En Windows (*símbolo del sistema o cmd*):

```Windows
python --version
```

La versión debe ser 3.7.0 o superior. Para actualizar Python ejecute el siguiente comando: `pip install python --upgrade`

También se requieren los módulos:

* [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)
* [Selenium 3](https://pypi.org/project/selenium/)

Para instalar los módulos, utilizar `pip`

**Beautiful Soup:**

`pip install beautifulsoup4`

**Selenium:**

`pip install selenium`

**Instalar Chromedriver**

* Descargar Chromedriver desde el [sitio oficial](http://chromedriver.chromium.org/downloads)
* Guardar el archivo en una carpeta, de preferencia del sistema. (En Windows, por ejemplo, puede guardarse en `C:\Program Files\Chromedriver`)
* **Agregar la ruta al PATH**. En Windows, la manera más segura para hacerlo es a través de la ventana *editar las variables del entorno del sistema* (la encuentras escribiendo *path* en el buscador del inicio), aplicar el botón `Variables del entorno...` y en la casilla `Variables del sistema` seleccionar `path` y `Editar`. Desde allí, seleccionar `Nuevo` y pegar la ruta donde guardate el archivo de Chromedriver (ej.: `C:\Program Files\Chromedriver`). *Puede ser necesario que hagas este mismo ejercicio con la ruta de `Python 3`*.

También puede utilizar el instalador creado por [Daniel Kaiser](https://github.com/danielkaiser) utilizando el siguiente comando en pip:

`pip install chromedriver-binary`

## Descargar el programa

Descarga el programa en cualquiera de las dos ligas disponible en <https://github.com/jairomelo/descargadores_archivos_hispanoamericanos/releases/tag/v1.0-beta>

## Iniciar el programa

### Windows

Descomprima el archivo \*.zip o \*.tar.gz
Doble clic sobre el archivo

### Mac y Linux

Descomprima el archivo \*.zip o \*.tar.gz
Desde la terminal, navega a la carpeta donde haya descargado el programa

Escriba el siguiente comando:

`python PARES_img_downloader-v.0.9.py`

## Uso del programa

**Ingresar número del expediente**: Corresponde al número del expediente en el catálogo. Por ejemplo, la signatura `INDIFERENTE,1342A,N.1` (*Expediente causado con motivo de ciertas noticias...*) corresponde al enlace <http://pares.mcu.es/ParesBusquedas20/catalogo/show/7287919> En este caso, el número del expendiente es **7287919**. 

**cantidad de imágenes**: Corresponde al número de imágenes, desde la primera hasta la última. En el caso del expediente anterior serían 702. Es posible hacer descargas parciales (10, 50, 100 imágenes), pero no es posible escoger un bloque o sección de imágenes.

Al dar `Enter` el programa se ejecutará. Abrirá un navegador automatizado y posteriormente comenzará a descargar las imágenes en una carpeta con el número del expediente.

Al finalizar, el programa se cerrará automáticamente.

## Soporte

<https://github.com/jairomelo/descargadores_archivos_hispanoamericanos/issues>