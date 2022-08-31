import pandas as pd
from fastapi import Fast API

app = FastAPI()

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

@app.get("/{user}")
def index(user):
    return str(user=='Bradford') + '\n'

@app.get("/medians/{filename}")
def summary(filename):
    thedata=readpandas(filename)
    return str(thedata.median(axis=0))