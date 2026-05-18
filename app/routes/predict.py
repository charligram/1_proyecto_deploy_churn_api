from fastapi import APIRouter
from app.schemas.usuario import Usuario
from app.schemas.response import ResponseModel
from app.services.model_service import predict_churn

# Router con función/post de predicción
router = APIRouter()


# Esta ruta es la que devuelve el json a la app
@router.post("/predict", response_model=ResponseModel)
def predict(usuario: Usuario): 
    
    prediccion = predict_churn(usuario)

    return {
        "prediccion": int(prediccion)
    }