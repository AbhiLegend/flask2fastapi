from fastapi import FastAPI

app = FastAPI()

@app.get("/{number}")
def index(number):
    return str(int(number)+1)+'\n'