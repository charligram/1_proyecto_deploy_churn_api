from fastapi import APIRouter
from app.schemas.usuario import Usuario

# Router con función/post de predicción
router = APIRouter()

# Esta ruta es la que devuelve el json a la app
@router.post("/predict")
def predict(usuario: Usuario): 
    pass