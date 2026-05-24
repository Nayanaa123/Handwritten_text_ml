import pandas as pd
from PIL import Image
import io
import random

df = pd.read_parquet("datasets/train-00000-of-00001.parquet")

text_input = input("Enter text: ").lower()

matches = []

for i in range(len(df)):
    txt = str(df.iloc[i]["text"]).lower()

    if any(word in txt for word in text_input.split()):
        matches.append(i)

if len(matches) == 0:
    print("No matching handwriting found")
    exit()

index = random.choice(matches)

img_bytes = df.iloc[index]["image"]["bytes"]

img = Image.open(io.BytesIO(img_bytes))

img.save("output.png")

print("Saved as output.png")