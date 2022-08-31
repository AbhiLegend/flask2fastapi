import pandas as pd
from fastapi import FastAPI

app = FastAPI()

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

@app.get('/{user}')
def index(user):
    return "Hello " + user

@app.get('/size/{filename}')
def size(filename):
    thedata=readpandas(filename)
    return str(len(thedata.index))

@app.get('/summary/{filename}')
def summary(filename):
    thedata=readpandas(filename)
    return str(thedata.mean(axis=1))