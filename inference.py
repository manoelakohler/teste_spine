# Estamos em ambiente de produção.

# 1. Carregaremos o modelo treinado
# 2. Carregaremos novos dados a serem inferidos
# 3. Faremos as inferências
# 4. Salvamos inferências em um csv
# 5. FIM

import joblib
import pandas as pd

# 1. Carregaremos o modelo treinado
filename = 'model/spine_model.pkl'
model = joblib.load(open(filename, 'rb'))

# 2. Carregaremos novos dados a serem inferidos
new_data = pd.read_csv('data/Dataset_spine_unknown.csv')

# 3. Faremos as inferências
inferences = model.predict(new_data)

# 4. Se quiser salvar em um csv
new_data['previsoes'] = inferences
pd.DataFrame(new_data).to_csv('model/inferences.csv', index=False)
print(inferences)

# FIM