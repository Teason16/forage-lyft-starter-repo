from abc import ABC, abstractmethod


class rentalCar(ABC):
    def __init__(self, current_date, current_mileage, engine, battery, last_service_date, last_service_mileage):
        self.current_date = current_date
        self.current_mileage = current_mileage        
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
