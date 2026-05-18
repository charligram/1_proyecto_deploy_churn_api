import joblib
from app.schemas.usuario import Usuario
import pandas as pd
from src.preprocessing import preprocess_data

# Cargar modelo entrenado
model_random_forest = joblib.load("model/churn_model_randomforest.pkl")

# Columnas con las que se entrenó
train_columns = joblib.load("model/model_columns.pkl")


# Función que recibe un usuario y genera una predicción (usada por routes)
def predict_churn(usuario: Usuario):

    # Crear dataframe con cada valor del usuario
    data = pd.DataFrame([
        {
            "customerID": usuario.customerID,
            "gender": usuario.gender,
            "SeniorCitizen": usuario.SeniorCitizen,
            "Partner": usuario.Partner,
            "Dependents": usuario.Dependents,
            "tenure": usuario.tenure,
            "PhoneService": usuario.PhoneService,
            "MultipleLines": usuario.MultipleLines,
            "InternetService": usuario.InternetService,
            "OnlineSecurity": usuario.OnlineSecurity,
            "OnlineBackup": usuario.OnlineBackup,
            "DeviceProtection": usuario.DeviceProtection,
            "TechSupport": usuario.TechSupport,
            "StreamingTV": usuario.StreamingTV,
            "StreamingMovies": usuario.StreamingMovies,
            "Contract": usuario.Contract,
            "PaperlessBilling": usuario.PaperlessBilling,
            "PaymentMethod": usuario.PaymentMethod,
            "MonthlyCharges": usuario.MonthlyCharges,
            "TotalCharges": usuario.TotalCharges
        }
    ])

    # Preprocesar
    data = preprocess_data(data)

    # Quitar columna innecesaria
    data = data.drop(columns=["customerID"])

    # Obtener dummies
    data = pd.get_dummies(data)

    # Igualar la data a las columnas con las que se entrenó
    data = data.reindex(
        columns=train_columns,
        fill_value=0
    )

    # Generar predicción
    prediccion = model_random_forest.predict(data)[0]

    return prediccion