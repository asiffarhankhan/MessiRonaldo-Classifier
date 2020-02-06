import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

batch_size = 16
path = 'dataset/test'
imgen = ImageDataGenerator(rescale=1/255.)
testGene = imgen.flow_from_directory(directory=path,
                                        target_size=(150, 150,),
                                        shuffle=False,
                                        class_mode='binary',
                                        batch_size=batch_size,
                                        save_to_dir=None
                                        )

model = tf.keras.models.load_model("classifier.h5")
pred = model.predict_generator(testGene, steps=testGene.n/batch_size)

print(pred)