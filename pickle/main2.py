import pandas as pd
import pickle
from fastapi import FastAPI

app = FastAPI()

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

@app.get('/prediction')
def prediction():
    thedata=pd.read_csv('predictiondata.csv')
    with open('deployedmodel.pkl', 'rb') as file:
        themodel = pickle.load(file)
    prediction=themodel.predict(thedata)
    return str(prediction)