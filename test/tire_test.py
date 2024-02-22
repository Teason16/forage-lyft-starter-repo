import unittest

from tire.carrigan_tires import CarriganTires
from tire.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0.8, 0.9, 0.8, 0.8]
        tires = CarriganTires(sensor_array)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        sensor_array = [0.4, 0.4, 0.4, 0.4]
        tires = CarriganTires(sensor_array)
        self.asserFalse(tires.needs_service())
     
        
class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTires(sensor_array)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        sensor_array = [0.4, 0.4, 0.4, 0.4]
        tires = OctoprimeTires(sensor_array)
        self.asserFalse(tires.needs_service())