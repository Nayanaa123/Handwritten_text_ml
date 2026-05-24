import pandas as pd
from PIL import Image
import io
import os

df = pd.read_parquet("datasets/train-00000-of-00001.parquet")

os.makedirs("sample_images", exist_ok=True)

for i in range(5):
    img_bytes = df.iloc[i]["image"]["bytes"]
    img = Image.open(io.BytesIO(img_bytes))
    img.save(f"sample_images/sample_{i}.png")

print("Saved successfully")