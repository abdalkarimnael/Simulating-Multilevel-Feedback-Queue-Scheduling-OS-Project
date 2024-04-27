class Process:
    def __init__(self, pid, arrival_time):
        self.__pid = pid
        self.__arrivalTime = arrival_time
        self.__bursts = []
        self.__workingTime = 0
        self.__finishTime = 0
        self.__count = 0
        self.__predictTime = 20 # tau(n)

    def get_pid(self):
        return self.__pid

    def set_pid(self, pid):
        self.__pid = pid

    def get_arrival_time(self):
        return self.__arrivalTime

    def set_arrival_time(self, arrival_time):
        self.__arrivalTime = arrival_time

    def get_bursts(self) -> list:
        return self.__bursts

    def set_bursts(self, bursts: list):
        self.__bursts = bursts

    def get_working_time(self):
        return self.__workingTime

    def set_working_time(self, t):
        self.__workingTime = t

    def get_finish_time(self):
        return self.__finishTime

    def set_finish_time(self, finish_time):
        self.__finishTime = finish_time

    def get_count(self):
        return self.__count

    def get_predict_time(self):
        return self.__predictTime

    def set_predict_time(self, predict_time):
        self.__predictTime = predict_time

    def set_count(self, count):
        self.__count = count

    def __lt__(self, other):
        return self.__arrivalTime < other.__arrivalTime

    def __repr__(self):
        process_str = '{}\t{}\t{}'.format(self.__pid, self.__arrivalTime, "\t".join(str(burst) for burst in self.__bursts))
        return process_str

    def __str__(self):
        return f'pid: {self.__pid}\nArrival Time: {self.__arrivalTime}\nBursts: {self.__bursts}\n'