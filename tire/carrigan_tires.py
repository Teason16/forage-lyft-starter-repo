from tire.tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        for wear in sensor_array:
            if wear >= 0.9:
                return True
            else:
                return False