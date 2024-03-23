from Consumer import Consumer_
from Producer import Producer_
from catboost import CatBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import json

consumer = Consumer_(bootstrap_servers = 'localhost:9097', topic = 'processed_data', group_id = 'model' )
consumer.subscribe_on_topic() 
producer = Producer_(bootstrap_servers = 'localhost:9094', topic = 'resultsML')

model = CatBoostRegressor()
model.load_model('./models/catboost_model.cbm')

while True:
    msg = consumer.get_messages(10)
    if msg != -1:
        data = json.loads(msg.value().decode('utf-8')) 
        prediction = model.predict(data["features"]).tolist() 
        
        mse = mean_squared_error(data["target"], prediction)
        mae = mean_absolute_error(data["target"], prediction)

        metrics = {'age': prediction, 'metrics' : {"MSE": mse, "MAE": mae}} 
        
        producer.produce_message(message_key='1', message_value=json.dumps(metrics)) 
        producer.flush()


