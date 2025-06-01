import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle

# Load pre-trained CNN (VGG16) model
def extract_features(img_path):
    model = VGG16()
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    feature = model.predict(x, verbose=0)
    return feature

# Load tokenizer and LSTM model
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
caption_model = load_model("caption_model.h5")

# Generate captions
def generate_caption(photo, max_length=34):
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = caption_model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = tokenizer.index_word.get(yhat, None)
        if word is None or word == 'endseq':
            break
        in_text += ' ' + word
    return in_text.replace('startseq', '').strip()

# Test the model
img_path = 'example.jpg'  # Replace with your image
feature = extract_features(img_path)
caption = generate_caption(feature)
print("Generated Caption:", caption)

# Show the image with caption
img = image.load_img(img_path)
plt.imshow(img)
plt.title(caption)
plt.axis('off')
plt.show()
