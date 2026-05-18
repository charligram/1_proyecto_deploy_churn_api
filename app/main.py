from fastapi import FastAPI
from app.routes.predict import router

# Aplicación
app = FastAPI()

# Incluir el router de routes/, que contiene el endpoint para hacer predicciones
app.include_router(router)


# Ruta inicial/raíz
@app.get("/")
def inicio():
    return {
        "Status": "API works"
    }