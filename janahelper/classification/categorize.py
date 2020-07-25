import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sw = stopwords.words('english')

import pickle
with open('D:\\JPMC-Hack\\team-25\\janahelper\\classification\\tokenizer.pickle', 'rb') as handle:                                  ## Load tokenizer
    tokenizer = pickle.load(handle)

import tensorflow as tf 

from nltk.stem import WordNetLemmatizer  
lemmatizer = WordNetLemmatizer() 
m = tf.keras.models.load_model('D:\\JPMC-Hack\\team-25\\janahelper\\classification\\m.h5')                                          ## Load model file

y=['Mobility - Roads, Footpaths and Infrastructure',         
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
         'Fire Safety',]

from sklearn.preprocessing import LabelEncoder                                   
labelEncoder = LabelEncoder()
output = labelEncoder.fit_transform(y)                                          ## Convert categories to numerical values

def pred(sentence):
    sentence=[sentence]
    for x in range(len(sentence)):                                              ## remove stopwards and lemmatize
        print(x)
        s=sentence[x].split()
        s1=[]
        for i in s:
            if(i not in sw):
                s1.append(lemmatizer.lemmatize(i))
        sentence[x]=' '.join(s1)


    test = tokenizer.texts_to_sequences(sentence)                               ## tokenize sentence and pad 0s
    test = pad_sequences(test,maxlen=14)

    x=labelEncoder.inverse_transform([np.argmax(m.predict(test))])              ## Predict
    print(x[0])

    return x[0]                                                                  ## Return prediction
