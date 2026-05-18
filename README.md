# 💻 Predicción de churn API
Esta API está desarrollada con el fin de identificar el abandono de clientes de servicios de internet/telefonía (Churn)

## ℹ️ Dataset
Recurso: Kaggle

## 🎯 Objetivo
Desplegar proyecto de predicción de churn

Identificar abandono mediante características como:
- Tipo de contrato
- Tenencia de soporte técnico
- Contratos de servicios de internet
- Método de pago
- Etc.

## 📂 Tecnologías utilizadas
- Python
- Scikit-learn
- Pandas
- FastAPI
- Uvicorn
- Joblib
- Pydantic

## ⚙️ Funcionamiento del proyecto
1. Entrenamiento del modelo
- Ejecutar "python -m model.train"

2. Puesta en marcha
- Ejecutar "uvicorn app.main:app --reload"

3. Docs
- Documentación Swagger en http://127.0.0.1:8000/docs

4. Endpoint
- POST /predict

Ejemplo de request:

{
  "customerID": "7795-CFOCW",
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 45,
  "PhoneService": "No",
  "MultipleLines": "No phone service",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "No",
  "DeviceProtection": "Yes",
  "TechSupport": "Yes",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "One year",
  "PaperlessBilling": "No",
  "PaymentMethod": "Bank transfer (automatic)",
  "MonthlyCharges": 42.3,
  "TotalCharges": "1840.75"
}

Ejemplo de response:

{
  "prediccion": 1
}

1: Cliente con posibilidad de churn

0: Cliente con poco riesgo de churn

## ❗ Detalles
- Se recomienda generar ambiente virtual venv con python 3.11
- Es necesario crear carpeta "data" al mismo nivel de app, model, src. Dentro de ella crear carpeta "raw", dentro de raw descargar dataset disponible en https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Posibles mejoras futuras
- Implementación de docker
- Pipeline completo con scikit-learn pipeline
- Validación avanzada de inputs

## 👤 Autor
Carlos Rojas Villegas