import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(bootstrap_servers=['13.60.168.132:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

df = pd.read_csv("data/postings.csv")

for index, row in df.iterrows():
    dict_stock = row.to_dict()
    producer.send('demo_test', value=dict_stock)
    sleep(1)

