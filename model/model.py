from datetime import datetime
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from rentalCar import rentalCar

model = rentalCar(10/15/2000, 150000, CapuletEngine, SpindlerBattery, 8/1/2000, 120000)
print(model.engine.needs_service)
