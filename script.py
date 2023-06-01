import sys
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the SavedModel
model = tf.saved_model.load("C:/Users/aysul/OneDrive/Рабочий стол/final_model/")
class_names = ["Acne and Rosacea", "Actinic Keratosis Basal Cell Carcinoma", "Atopic Dermatitis", "Bullous Disease", "Cellulitis Impetigo", "Eczema", "Exanthems and Drug Eruptions", "Hair Loss Photos Alopecia", "Herpes HPV and other STDs", "Light Diseases and Disorders of Pigmentation", "Lupus and other Connective Tissue diseases", "Melanoma Skin Cancer Nevi and Moles", "Nail Fungus and other Nail Disease", "Poison Ivy Photos and other Contact Dermatitis", "Psoriasis pictures Lichen Planus and related diseases", "Scabies Lyme Disease and other Infestations and Bites", "Seborrheic Keratoses and other Benign Tumors", "Systemic Disease", "Tinea Ringworm Candidiasis and other Fungal Infections", "Urticaria Hives", "Vascular Tumors", "Vasculitis Photos", "D:/homework/our-AI-project/Dataset/Train/Warts Molluscum and other Viral Infections"]

# Preprocess the image
def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((180, 180))  # Resize the image to match the model's input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = tf.expand_dims(image, axis=0)  # Add a batch dimension
    return image

# Load and preprocess the image
image_path = "C:/Users/aysul/OneDrive/Рабочий стол/image.jpg"
input_image = preprocess_image(image_path)

# Perform inference
output = model(input_image)

# Process the output to get the predicted class
predicted_class_index = tf.argmax(output, axis=1).numpy()[0]
predicted_class = class_names[predicted_class_index]

# Print the predicted class
print(predicted_class)

