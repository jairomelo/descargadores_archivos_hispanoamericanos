# Descargador de archivos hispanoamericanos

A pesar de los importantes esfuerzos que han realizado los archivos históricos y bibliotecas patrimoniales en hispanoamérica para poner a disposición de los investigadores, estudiantes y público en general, sus acervos documentales y bibliográficos; aún son muchas las ocasiones en las cuales requerimos trabajar con dichos acervos fuera de línea. Aunque algunas plataformas digitales permiten la descarga masiva de recursos, en muchas otras nos encontramos con la obligación de consultarlos en línea, no siempre con la mayor velocidad o presentación disponible.

La posibilidad de descargar los documentos permite que el usuario pueda ganar autonomía al almacenarlos en su equipo personal, donde puede manipularlos, editarlos y compartirlos de manera más sencilla.

## Objetivo

Construir una aplicación que permita la descarga masiva de recursos digitales disponibles en bibliotecas patrimoniales y archivos históricos hispanoamericanos, con fines de investigación y consulta.

## ¿Es esto legal?

La técnica que se utiliza se denomina *Web Scrapping*, es decir, una recolección automatizada de recursos que ya están disponibles de manera abierta en la Web. Lo único que pretende el programa es automatizar un proceso que de otra manera implicaría realizar una tarea repetitiva de manera manual.

Es decir, con estos programas no se pretende recolectar información no autorizada al usuario, protegida por contraseñas, o que pueda implicar romper con la seguridad del sitio.

## Archivos y bibliotecas objetivo:

- **PARES: El Portal de Archivos Españoles.** Descarga automatizada de legajos disponibles en su repositorio. Actualmente se encuentra disponible una [versión beta estable](https://github.com/jairomelo/descargadores_archivos_hispanoamericanos/tree/pares-0.9) y una [versión de desarrollo](https://github.com/jairomelo/descargadores_archivos_hispanoamericanos/tree/pares-desarrollo).

- **Archivo General de la Nación de Colombia.** Descarga automatizada de imágenes por legajo. Actualmente en una versión preliminar. En desarrollo, una versión estable para descarga en formato PDF aprovechando el script de la página.

- **Hemeroteca digital del periódico Vanguardia Liberal.** Descarga simple automatizada por fecha (un periódico a la vez). Actualmente una versión preliminar. En desarrollo, una versión estable para descargar en rango de fechas.

*Los siguientes repositorios sólo están en modo de propuesta*

- **Biblioteca Nacional de Colombia.** Descarga de documentos PDF por criterios de búsqueda.
- **Hemeroteca Digital Hispánica.** Descarga de documentos PDF por criterios de búsqueda y rangos de fecha. Sólo para documentos que cumplan con el criterio público.
- **FamilySearch.** Descarga masiva de legajos digitalizados. Requiere usuario y contraseña de usuario.
- **Hemeroteca Nacional Digital de México.** Descarga de documentos PDF por criterio de búsqueda, rangos de fecha y títulos de periódicos. Sólo para documentos que cumplan con el criterio público.

Si desea que otro archivo o biblioteca sea incluido puede decirnos en la pestaña [issues](https://github.com/jairomelo/descargadores_archivos_hispanoamericanos/issues).

## Aspectos técnicos

Los programas se están escribiendo en [Python3](https://www.python.org/downloads/), por lo que los usuarios de Windows deberán instalar primero el entorno de Python para poder ejecutarlos.
En este momento, se requiere la instalación de módulos adicionales para la ejecución de los programas, por lo cual se recomienda conocer el uso de `pip` y configuración de las variables del entorno del sistema.

*Se está trabajando en un instalador para Windows con el propósito de hacer más amigable al usuario el uso del software.*

## Advertencia

Es responsabilidad del usuario el uso correcto del programa. No los ejecute desde carpetas que contengan información importante. Se recomienda crear una carpeta vacía desde la cual ejecutar el programa. 

## Solución de problemas

Puede consultar o incluir errores en la pestaña [issues](https://github.com/jairomelo/descargadores_archivos_hispanoamericanos/issues).

## Licencia

El software que se encuentra en producción y del que aquí resulte se encuentra publicado bajo una licencia [CeCILL v2.1](https://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html), compatible con [GNU/GPL](https://www.gnu.org/licenses/gpl-3.0.html) y aprobada por la [FSF](https://www.fsf.org/) y la [OSI](http://opensource.org/).

El *descargador de archivos hispanoamericanos* se publica bajo una [licencia MIT](https://github.com/UniversalViewer/universalviewer/blob/master/LICENSE.txt).

## Contacto

En este momento el proyecto es mantenido por Jairo A. Melo ([jairomelo](https://github.com/jairomelo))