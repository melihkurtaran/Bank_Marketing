import pickle
import pandas as pd
import json

def predict_mpg(config):
    ##loading the model from the saved file
    pkl_filename = "model.pkl"
    with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)

    if type(config) == dict:
        x = pd.DataFrame([config])
    else:
        x = config
   
    y_pred = str(int(model.predict(x)))
    
    return y_pred