import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Cargar MobileNetV2 preentrenado sin las capas finales
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')

# Congelar las capas preentrenadas
base_model.trainable = False

# Crear el modelo final con capas adicionales
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')  # 3 clases: feliz, triste, enojado
])

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocesamiento de las imágenes
train_datagen = ImageDataGenerator(rescale=1.0/255.0)
val_datagen = ImageDataGenerator(rescale=1.0/255.0)

# Cargar las imágenes de entrenamiento
train_generator = train_datagen.flow_from_directory(
    'dataset/train',  # Ruta a tu conjunto de datos de entrenamiento
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Cargar las imágenes de validación
validation_generator = val_datagen.flow_from_directory(
    'dataset/validation',  # Ruta a tu conjunto de datos de validación
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Entrenar el modelo
model.fit(
    train_generator,
    steps_per_epoch=100,  # Número de lotes por época (ajustar según el tamaño del dataset)
    epochs=10,            # Número de épocas
    validation_data=validation_generator,
    validation_steps=50   # Número de pasos de validación (ajustar según el tamaño del dataset)
)

# Guardar el modelo entrenado
model.save('model/emotion_model.h5')  # Guardar el modelo para usarlo luego en el backend
