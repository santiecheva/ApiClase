from fastapi import FastAPI

app = FastAPI()

@app.get("/hola")
def hola():
    return {"message":"Hola clase"}