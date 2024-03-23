import subprocess

class ProcessManager:
    def __init__(self, python_path='./myenv/bin/python') -> None:
        self.__python_path = python_path
        self.__processes = {}

    @property
    def python_path(self,) -> str:
        return self.__python_path

    @property
    def processes(self,) -> dict:
        return self.__processes 
    
    @python_path.setter
    def python_path(self, new_path: str) -> None:
        self.__python_path = new_path

    def __start_docker_compose(self) -> None:
        subprocess.run(["docker-compose", "up", "-d"])

    def __stop_docker_compose(self) -> None:
        subprocess.run(["docker-compose", "down"]) 

    def __start_process(self, name: str, command: list) -> None:
        self.__processes[name] = subprocess.Popen(command)

    def __start_processes(self,) -> None:
        self.__start_process('SendData', [self.__python_path, "./src/backend/DataSendKafka.py"])
        self.__start_process('PreprocessingData', [self.__python_path, "./src/backend/preprocessing.py"])
        self.__start_process('ML', [self.__python_path, "./src/backend/ML.py"])
        self.__start_process('VisualizationResults', [self.__python_path, "-m", "streamlit", "run", "./src/frontend/visualization.py"])

    def __stop_processes(self,) -> None:
        for process in self.__processes.values(): 
            process.kill() 

    def run(self,) -> None:
        try: 
            self.__start_docker_compose()
            self.__start_processes()
            while True: 
                continue 
        except KeyboardInterrupt: 
            print("Stopping...")
            self.__stop_processes()
            self.__stop_docker_compose()


if __name__ == '__main__':
    process_manager = ProcessManager()
    process_manager.run()