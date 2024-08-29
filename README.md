# Detecção de Anomalias na Coluna Vertebral

Este projeto implementa um modelo de machine learning para prever anomalias na coluna vertebral usando um classificador de árvore de decisão. O modelo é treinado com um conjunto de dados de medições da coluna e fornece previsões sobre se uma coluna é "Anormal" ou "Normal". O projeto também inclui uma API para fazer previsões com base no modelo treinado.


## Pré-requisitos

Para executar este projeto, você precisa ter o Python 3.10.11 instalado com as bibliotecas do arquivo requirements.txt. Você pode instalar as dependências usando o seguinte comando:

```pip install -r requirements.txt ```

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

├── data 

│ └── Dataset_spine.csv # Conjunto de dados usado para treinamento e teste 

├── model 

│ ├── spine_model.pkl # Modelo treinado 

│ └── spine_tree.png # Visualização da árvore de decisão 

├── train.py # Script para treinar o modelo e gerar visualizações 

└── api.py # API baseada em FastAPI para realizar previsões