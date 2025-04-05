import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

# Load Model
model = load_model('gemstones10_model.h5')
categories = ['Alexandrite', 'Ametrine', 'Andalusite', 'Andradite', 'Aquamarine', 'Aventurine Green', 'Aventurine Yellow', 'Benitoite', 'Beryl Golden', 'Carnelian', 'Cats Eye', 'Chalcedony', 'Chalcedony Blue', 'Coral', 'Diaspore', 'Dumortierite', 'Emerald', 'Fluorite', 'Garnet Red', 'Goshenite', 'Grossular', 'Hessonite', 'Hiddenite', 'Iolite', 'Jade', 'Jasper', 'Kunzite', 'Kyanite', 'Labradorite', 'Lapis Lazuli', 'Larimar', 'Malachite', 'Moonstone', 'Morganite', 'Opal', 'Pearl', 'Peridot', 'Pyrite', 'Pyrope', 'Quartz Beer', 'Quartz Rose', 'Quartz Rutilated', 'Rhodochrosite', 'Rhodolite', 'Sapphire Blue', 'Sunstone', 'Tanzanite', 'Variscite', 'Zircon', 'Zoisite']  # Replace with actual category names

# Streamlit App
st.title("Gemstones Classification App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Make prediction
    predictions = model.predict(image_array)
    predicted_class = categories[np.argmax(predictions)]

    st.write(f"Predicted Class: {predicted_class}")





#python -m streamlit run app.py

