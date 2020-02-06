import numpy as np
from keras.preprocessing import image
import tensorflow as tf 

category = ['Messi', 'Ronaldo']
model = tf.keras.models.load_model('classifier.h5')
img_width, img_height = 150, 150
img = image.load_img('dataset/test/sample/test11.jpeg', target_size = (img_width, img_height))
img = image.img_to_array(img)
img = np.expand_dims(img, axis = 0)

prediction = model.predict(img)
print(category[int(prediction)])