## Ejemplo para bajar un video de YouTube

*Probado en Windows y Linux*

Para poder ejecutar correctamente el ejemplo, se recomienda `python3` e instalar las siguientes librerías:

```python
## Puede ser que esta librería ya lo tenga instalada
pip install Tkinter

## Esta librería es el que realmente realiza la tarea
pip install PyTube
```

El siguiente código se ha cambiado para poder obtener la calidad del video:

```python
# Corresponde a la posición en la lista de resoluciones
video = url.streams.filter(progressive=True).last()

# Con el siguiente código se descarga el archivo con mayor resolución
video = url.streams.get_highest_resolution()

# Bajar el video según la lista disponible
video = url.streams[1]
```

Este código lo he obtenido de las siguientes rutas:

* [Creating a simple YouTube Video Downloader using Python | Engineering Education (EngEd) Program | Section](https://www.section.io/engineering-education/youtube-video-downloader-using-python/)

* [GitHub - Patalin/YouTube-Downloader](https://github.com/Patalin/YouTube-Downloader)

## Errores:

Si al momento de ejecutar el aplicativo sale el siguiente error:

```python
pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
```

Se debe cambiar la siguiente línea de la librería `pytube`, específicamente, en el archivo `cipher.py`:

```python
## Línea a modificar
var_regex = re.compile(r"^\w+\W")
## Por esta
var_regex = re.compile(r"^\$*\w+\W")
```

Se puede realizar el cambio en el archivo que se encuentra en la ruta del proyecto:

* Linux: `[RUTA_RAIZ]/YouTube-Downloader/venv/lib/python3.8/site-packages/pytube`

* Windows: `[RUTA_RAIZ]\YouTube-Downloader\venv\Lib\site-packages\pytube`

*Fuente:*

[python - pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W - Stack Overflow](https://stackoverflow.com/questions/70776558/pytube-exceptions-regexmatcherror-init-could-not-find-match-for-w-w)
