import pandas as pd
import os
import random

# Path to the image dataset
image_dir = "data/PlantVillage"
output_path = "data/environmental_features.csv"

# Collect image filenames and generate random environmental features
data = []

for label in os.listdir(image_dir):
    label_folder = os.path.join(image_dir, label)
    if os.path.isdir(label_folder):
        for img_name in os.listdir(label_folder)[:50]:  # Take a sample (up to 50 images per class)
            temperature = round(random.uniform(20, 35), 1)  # Random temperature between 20 and 35°C
            humidity = round(random.uniform(40, 90), 1)     # Random humidity between 40% and 90%
            soil_type = random.choice([1, 2, 3])            # Soil type: 1 = clay, 2 = sandy, 3 = silt

            data.append({
                "filename": img_name,
                "temperature": temperature,
                "humidity": humidity,
                "soil_type": soil_type,
                "label": label
            })

# Save the generated data to CSV
df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
df.to_csv(output_path, index=False)

print(f"CSV file created: {output_path} with {len(df)} rows")
