from confluent_kafka import Producer

class Producer_():
    def __init__(self, bootstrap_servers: str, topic: str) -> None:
        self.__bootstrap_servers = bootstrap_servers
        self.__topic = topic
        self.__producer = Producer({"bootstrap.servers": self.__bootstrap_servers })
    
    @property
    def bootstrap_servers(self,) -> str:
        return self.__bootstrap_servers
    
    @property
    def topic(self,) -> str:
        return self.__topic
    @property
    def producer(self,) -> Producer:
        return self.__producer

    def delivery_report(self, error: dict, message: dict):
        if error is not None:
            print(f"Error sending the message: {error}")
        else:
            print(f"The message was successfully sent to the topic: {message.topic()}")
    
    def produce_message(self, message_key: str, message_value: str) -> None:
        self.__producer.produce(
            self.topic,
            key = str(message_key),
            value=str(message_value),
            callback=self.delivery_report
        )
    
    def flush(self,) -> None:
        self.__producer.flush()