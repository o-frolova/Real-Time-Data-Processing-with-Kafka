from Producer import Producer_
import pandas as pd
import json
import time

dataset = pd.read_csv('./data/FinalDataset.csv')

producer_1 = Producer_(bootstrap_servers = 'localhost:9094', topic = 'raw_data')
producer_2 = Producer_(bootstrap_servers = 'localhost:9094', topic = 'raw_data')

for index, (row1, row2) in enumerate(zip(dataset.iloc[::2].itertuples(), dataset.iloc[1::2].itertuples())):

    producer_1.produce_message(message_key='1', message_value=json.dumps(row1)) 
    producer_2.produce_message(message_key='1', message_value=json.dumps(row2)) 

    producer_1.flush() 
    producer_2.flush()

    time.sleep(1)

