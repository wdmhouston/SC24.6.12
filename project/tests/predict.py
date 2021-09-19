import unittest
from modules.model import model

model1 = model()
image_path = "/data/SC24.6.12/project/data/data3/apple/Image_1.jpg"
print(model1.predict(image_path))
