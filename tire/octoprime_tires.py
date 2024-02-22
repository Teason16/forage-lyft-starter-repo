from tire.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        sum = 0
        for wear in sensor_array:
            sum += wear
        if sum >= 3:
            return True
        else:
            return False