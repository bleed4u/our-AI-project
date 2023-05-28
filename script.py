import sys
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the SavedModel
model = tf.saved_model.load("C:/Users/aysul/OneDrive/Рабочий стол/final_model/saved_model.pb")

# Preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))  # Resize the image to match the model's input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = tf.expand_dims(image, axis=0)  # Add a batch dimension
    return image

# Load and preprocess the image
image_path = sys.argv[1]
input_image = preprocess_image(image_path)

# Perform inference
output = model(input_image)

# Process the output
result = tf.argmax(output, axis=1).numpy()[0]

# Convert the result to a string
result_str = str(result)

# Print or return the result
print(result_str)
