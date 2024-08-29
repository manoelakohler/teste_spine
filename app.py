import joblib
import pandas as pd
from fastapi import FastAPI, UploadFile, File


app = FastAPI(docs_url='/', title="Deploy DM BIMaster - PUC-Rio")

# Carregar modelo
model = joblib.load('model/spine_model.pkl')


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """ Endpoint para previsão de anormalidade na coluna vertebral."""
    # Ler o arquivo
    df = pd.read_csv(file.file)
    # Fazer a predição
    predictions = model.predict(df)
    return {"Predictions": predictions.tolist()}
