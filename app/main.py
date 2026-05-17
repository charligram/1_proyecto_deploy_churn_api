from fastapi import FastAPI

# Aplicación
app = FastAPI()

# Ruta inicial/raíz
@app.get("/")
def inicio():
    return {
        "Status": "API works"
    }