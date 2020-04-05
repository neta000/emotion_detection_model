from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

import tensorflow as tf

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(input_details)
print(output_details)
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(64,64))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 64, 64, 3)
	# center pixel data
	img = img.astype('float32')
	print(img)
	return img

img = load_image('s.jpg')
interpreter.set_tensor(input_details[0]['index'],img)

interpreter.invoke()
out = interpreter.get_tensor(output_details[0]['index'])

print(out[0])

print(out.dtype)
 
	
 
