# Proyecto de Detecció de Emociones

## Prerequisitos:

- Windows 11

- Python 3.11.9

- TensorFlow

## Instalación de librerías

Ejecutar las siguientes sentencias:

```bash
pip install flask tensorflow numpy pillow flask-cors
```

## Ejecución

Para entrenar el modelo se debe ejecutar la siguiente sentencia:

```bash
## Ejecutarlo en la raiz
python train_model.py
```

Luego de entrenar el modelo, se puede ejecuar el servicio web para probar el modelo entrenado:

```bash
## Ejecutarlo en la carpeta 'app'
cd app/
python app.py
```

## Pruebas

Para probar, se puede usar la herramienta `Postman` con el siguiente:

```json
{
    "tipo":"POST",
    "url":"http://127.0.0.1:5000/predict",
    "parametros": {
        "tipo":"form-data2",
        "param": {
            "key":"image",
            "tipo":"file",
            "value":"un archivo de una imagen de un perro"
        }
    }
} 
```