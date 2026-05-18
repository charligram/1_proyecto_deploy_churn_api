import pandas as pd
from src.preprocessing import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Ruta de data
data_route = rf"data\raw\WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Lectura de data
df = pd.read_csv(data_route)

# Preprocesamiento de la info con preprocessing.py
df = preprocess_data(df)

# Separar datos y target
X = df.drop(columns=['Churn', 'customerID'])
y = df['Churn']

# Separar entrenamiento de pruebas
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42, stratify=y)

# Imputar datos faltantes de train con su mediana
total_charge_median_train = X_train['TotalCharges'].median()
X_train['TotalCharges'] = X_train['TotalCharges'].fillna(total_charge_median_train)

# Imputar datos faltantes de test con su mediana
total_charge_median_test = X_test['TotalCharges'].median()
X_test['TotalCharges'] = X_test['TotalCharges'].fillna(total_charge_median_test)

# Obtener dummies
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

# Alinear columnas
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

# Modelo
random_forest_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    min_samples_split=10,
    class_weight='balanced'
)

# Entrenar
random_forest_model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(random_forest_model, "model/churn_model_randomforest.pkl")


# Ahora guardaremos las columnas, las cuales van a ser necesarias para cuando se quieran hacer predicciónes
# de datos nuevos que el modelo no ha visto, a través de la API
joblib.dump(X_train.columns.to_list(), "model/model_columns.pkl")

print("Modelo guardado correctamente")