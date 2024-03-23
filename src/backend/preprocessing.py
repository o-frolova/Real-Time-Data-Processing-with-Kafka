from Consumer import Consumer_
from Producer import Producer_
from sklearn.pipeline import Pipeline
import pandas as pd
import json
import joblib

consumer = Consumer_(bootstrap_servers = 'localhost:9094', topic = 'raw_data', group_id = 'data_processors')
consumer.subscribe_on_topic()
producer = Producer_(bootstrap_servers = 'localhost:9097', topic = 'processed_data')

COLUMNS_NAME = ['age', 'user_id', 'region_name', 'city_name', 'cpe_manufacturer_name',
                'cpe_model_name', 'cpe_type_cd', 'cpe_model_os_type', 'price', 'count',
                'Sum_req', 'PartofDay']

def full_nan_value(dataset: pd.DataFrame) -> pd.DataFrame:
    return dataset.fillna(0)

def convert_value_to_int(dataset: pd.DataFrame) -> pd.DataFrame:
    return dataset.astype(int)

def removing_unnecessary_columns(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset.drop(['city_name', 'cpe_model_os_type', 'cpe_model_name', 'region_name', 'cpe_manufacturer_name', 'cpe_type_cd', 'PartofDay'], axis=1, inplace=True)
    return dataset

def concert_categorical_data(dataset: pd.DataFrame) -> pd.DataFrame:
    categorical_features = ['region_name', 'cpe_manufacturer_name', 'cpe_type_cd', 'PartofDay']
    encoder = joblib.load('./models/onehot_encoder_model.joblib')
    encoded_data = encoder.transform(dataset[categorical_features])
    encoded_data = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(categorical_features))
    dataset = pd.concat([dataset, encoded_data], axis=1)
    return dataset


while True:
    msg = consumer.get_messages(timeout = 10)
    if msg != -1:
        dataset = json.loads(msg.value().decode('utf-8')) 
        dataset = pd.DataFrame(dataset[1:], index=COLUMNS_NAME).T
        
        processed_data = (dataset.pipe(full_nan_value)
                    .pipe(concert_categorical_data)
                    .pipe(removing_unnecessary_columns)
                    .pipe(convert_value_to_int))
        target = processed_data["age"].to_numpy().tolist() 
        features = processed_data.drop(columns=["age"]).to_numpy().tolist() 
        data = {"features": features, "target": target} 

        producer.produce_message(message_key='1', message_value=json.dumps(data)) 
        producer.flush() 

