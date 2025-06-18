
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model('../model/emotion_model.h5')  # Cargar el modelo entrenado

@app.route('/predict', methods=['POST'])
def predict():
    img_file = request.files['image']
    img = image.load_img(img_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    emotion = ['happy', 'sad', 'angry'][predicted_class[0]]
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
