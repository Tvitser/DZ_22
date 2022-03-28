from abc import ABC, abstractmethod


def call_logger(method):
    def logger(*args, **kwargs):
        print(f'{args[0].__class__.__name__} {method.__name__}')
    return logger


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    @call_logger
    def start_engine(self):
        pass

    @call_logger
    def stop_engine(self):
        pass

    @call_logger
    def move(self):
        pass

    @call_logger
    def stop(self):
        pass


class Car(Transport):
    @call_logger
    def start_engine(self):
        pass

    @call_logger
    def stop_engine(self):
        pass

    @call_logger
    def move(self):
        pass

    @call_logger
    def stop(self):
        pass


class Electroscooter(Transport):
    @call_logger
    def start_engine(self):
        pass

    @call_logger
    def stop_engine(self):
        pass

    @call_logger
    def move(self):
        pass

    @call_logger
    def stop(self):
        pass


class Person:
    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.start_engine()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
