import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_images(images):
    flattened = [img.flatten() / 255.0 for img in images]
    return np.array(flattened)

def preprocess_environmental_data(df, image_names):
    df = df.set_index('filename')
    selected_rows = df.loc[image_names]
    features = selected_rows.drop(columns=['label'], errors='ignore')
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features