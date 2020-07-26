from nltk.stem import WordNetLemmatizer
import tensorflow as tf
import os
import pandas as pd
import os
import pickle
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sw = stopwords.words('english')
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'tokenizer.pickle'), 'rb') as handle:  # Load tokenizer
    tokenizer = pickle.load(handle)


lemmatizer = WordNetLemmatizer()
m = tf.keras.models.load_model(
    os.path.join(dir_path, 'm.h5'))  # Load model file

y = ['Mobility - Roads, Footpaths and Infrastructure',
     'Garbage and Unsanitary Practices',
     'Traffic and Road Safety',
     'Water Supply and Services',
     'Animal Husbandry',
     'Pollution',
     'not found',
     'Maintenance/Renovation Of Heritage Sites',
     'Community Infrastructure and Services',
     'Electricity and Power Supply',
     'Parks & Recreation',
     'Others',
     'Railways',
     'Crime and Safety',
     'Public Toilets',
     'Storm Water Drains',
     'Lakes',
     'Certificates',
     'Streetlights',
     'Sewerage Systems',
     'Trees and Saplings',
     'Fire Safety', ]

labelEncoder = LabelEncoder()
# Convert categories to numerical values
output = labelEncoder.fit_transform(y)


def pred(sentence):
    sentence = [sentence]
    for x in range(len(sentence)):  # remove stopwards and lemmatize
        s = sentence[x].split()
        s1 = []
        for i in s:
            if(i not in sw):
                s1.append(lemmatizer.lemmatize(i))
        sentence[x] = ' '.join(s1)

    test = tokenizer.texts_to_sequences(
        sentence)  # tokenize sentence and pad 0s
    test = pad_sequences(test, maxlen=14)

    x = labelEncoder.inverse_transform([np.argmax(m.predict(test))])  # Predict

    return x[0]  # Return prediction
