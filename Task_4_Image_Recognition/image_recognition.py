
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
model = MobileNetV2(weights="imagenet")
img = image.load_img("image.jpg", target_size=(224,224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)
prediction = model.predict(img_array)
result = decode_predictions(prediction, top=1)
print("Prediction:")
for _, label, confidence in result[0]:
    print(label)
    print("Confidence:", round(confidence*100,2),"%")
with open("output.txt","w") as file:
    file.write("Prediction:\n")
    for _, label, confidence in result[0]:
        file.write(label+"\n")
        file.write("Confidence: "+str(round(confidence*100,2))+"%")
