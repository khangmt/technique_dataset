text1 =  ["Hello", "World", "Python", "Programming"]
text2 =  ["Hi", "Population", "C++", "Data"]
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import tensorflow_hub as hub
import os
os.environ["TFHUB_CACHE_DIR"] = "./data/tf_hub"
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
model = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5") 
def get_cosine_similarity(predictions , references):
    predict_embed = np.array(model(predictions))
    reference_embed = np.array(model(references))
    cosine_simi = cosine_similarity(predict_embed, reference_embed)
    return cosine_simi


cosine_simil = get_cosine_similarity(text1, text2)
print(cosine_similarity)