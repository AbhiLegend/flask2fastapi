from fastapi import FastAPI

app = FastAPI()

@app.get("/{user}")
def index(user):
    return "Hello " + user