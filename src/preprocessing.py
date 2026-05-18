import pandas as pd

def map_yes_no_binary(df):
    """
    Mapear feature que tenga como categorías solamente los valores de "Yes" y "No de forma binaria.

    Args:
        df (pd.DataFrame): Dataframe con features de "Yes" y "No" con palabras.

    Returns:
        df (pd.DataFrame): DataFrame con categorías binarias en los features con "Yes" y "No"
    """
    yes_and_no_columns = []

    for col in df.columns:
        if len(df[col].unique()) == 2:
            if ('Yes' in df[col].unique()) and ('No' in df[col].unique()):
                yes_and_no_columns.append(col)

    for col in yes_and_no_columns:
        df[col] = df[col].map({'No':0, 'Yes':1})

    return df

# Ahora aquí colocamos la lógica para preprocesar la información que teniamos en el notebook
def preprocess_data(df):

    # Vimos que primero teniamos que hacerle strip a los TotalCharges y luego pasarlo todo a numérico,
    # si en algun punto falla pasando algo a numérico lo deja NaN
    df['TotalCharges'] = df['TotalCharges'].str.strip()
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Luego mapeamos las columnas que sean yes/no
    df = map_yes_no_binary(df)

    # Además necesitamos convertir los géneros a binario
    df['gender'] = df['gender'].map({
        "Female":0,
        "Male":1
    })

    # Y listo, a este dataset solo se le aplican esas limpiezas
    return df