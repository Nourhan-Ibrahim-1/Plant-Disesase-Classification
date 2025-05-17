import os
import pandas as pd
import cv2

def load_images(image_dir, target_size=(128, 128)):
    images = []
    labels = []
    image_names = []

    for class_name in os.listdir(image_dir):
        class_path = os.path.join(image_dir, class_name)
        if os.path.isdir(class_path):
            for img_file in os.listdir(class_path):
                img_path = os.path.join(class_path, img_file)
                try:
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, target_size)
                    images.append(img)
                    labels.append(class_name)
                    image_names.append(img_file)
                except:
                    print(f"Could not read image: {img_path}")
    return images, labels, image_names

def load_environmental_features(csv_path):
    """
    Expects CSV with columns: filename, temperature, humidity, soil_type, etc.
    """
    return pd.read_csv(csv_path)
