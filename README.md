# Real-Time-Data-Processing-with-Kafka
The project is a real-time data processing system using Apache Kafka as the main component. The main goal of the project is to provide a scalable, reliable and efficient solution for processing streaming data.
## Project structure
    
    .
    ├── data  
    |   ├── DataCollection.ipynb           # File for data collection                    
    |   └── FinalDataset.csv               # Final dataset prepared for analysis and processing     
    ├── models
    |   ├── catboost_info                  
    |   ├── catboost_model.cbm             # File with trained CatBoost model
    |   └── onehot_encoder_model.joblib    # Serialized One-Hot encoder model
    ├── research
    |   └── EDA.ipynb                      # Notebook with Exploratory Data Analysis (EDA)
    ├── src
    |   ├── backend
    |   |   ├── __pycache__
    |   |   ├── Consumer.py                # Class for working with Kafka consumer
    |   |   ├── DataSendKafka.py           # File for sending data to Kafka
    |   |   ├── ML.py                      # File with machine learning part
    |   |   ├── Producer.py                # Class for working with Kafka producer
    |   |   ├── __init__.py
    |   |   └── preprocessing.py           # File for data preprocessing
    |   └── frontend
    |       └── visualization.py           # File for inference
    ├── README.md                          # File with project description
    ├── docker-compose.yaml                # File for setting up and running Docker containers
    ├── main.py                            # Main executable file of the project
    └── requirements.txt                   # The file with project dependencies
    
## Dataset
The final dataset was created based on data provided by <a href="https://www.kaggle.com/datasets/nfedorov/mts-ml-cookies/data?select=dataset_full.feather"> MTS </a>, with the main purpose of predicting the age of users. The final dataset contains only a part of the original data set, and preliminary processing has been carried out aimed at removing duplicate records about the same user. In addition, data analysis (EDA) was performed, which provided additional insight into the characteristics of the data and their relationships. As a result of these steps, a final dataset was formed, ready for further use in analysis and machine learning tasks.
## Run project
```bash
source ./venv/bin/activate
export PYTHONPATH=./src/backend:$PYTHONPATH
python main.py
```
## Demonstration

https://github.com/o-frolova/Real-Time-Data-Processing-with-Kafka/assets/128040555/bbbd9e16-dfc5-4b90-b806-4147d6716e03


