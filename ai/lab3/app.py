import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

mnist = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',

loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10, verbose=2)

i = np.random.randint(0, len(test_images))
img = test_images[i]

img = img.reshape(1, 28, 28)
prediction = model.predict(img)
detected_digit = np.argmax(prediction)

plt.imshow(img[0], cmap=plt.cm.binary)
plt.title(f"Digit: {test_labels[i]}, Detected Digit: {detected_digit}")
plt.show()