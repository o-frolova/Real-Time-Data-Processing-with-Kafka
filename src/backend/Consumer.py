from confluent_kafka import Consumer
class Consumer_():
    def __init__(self, bootstrap_servers: str, topic: str, group_id = None) -> None:
        self.__bootstrap_servers = bootstrap_servers
        self.__topic = topic
        self.__group_id = group_id
        self.__consumer = Consumer({"bootstrap.servers": self.__bootstrap_servers, 'group.id': self.__group_id})
    
    @property
    def bootstrap_servers(self,) -> str:
        return self.__bootstrap_servers
    
    @property
    def topic(self,) -> str:
        return self.__topic

    @property
    def consumer(self,) -> str:
        return self.__consumer

    @property
    def group_id (self,) -> str:
        return self.__group_id 
    
    def subscribe_on_topic(self,) -> None:
        self.__consumer.subscribe([self.__topic])
    
    def get_messages(self, timeout: int) -> None:
        message = self.__consumer.poll(timeout)

        if message is None:
             print(f"The message is None")
             return -1
        elif message.error():
            print(f"Error receiving the message: {message.error()}")
            return -1
        else: 
            return message
    