
from tensorflow.keras.models import load_model
import tensorflow as tf


model = load_model('model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)


tflite_model = converter.convert()

file = open( 'model.tflite' , 'wb' ).write( tflite_model )