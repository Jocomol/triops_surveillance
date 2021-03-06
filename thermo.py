from w1thermsensor import W1ThermSensor
import datetime
import subprocess


class Thermo(W1ThermSensor):

    def __init__(self):
        W1ThermSensor.__init__(
            self,
            W1ThermSensor.THERM_SENSOR_DS18B20,
            "00000833e8ff")

    def read_measurement(self):
        meassuered_data = [str(datetime.datetime.now().isoformat())]
        meassuered_temps = (self.get_temperatures([
            self.DEGREES_C,
            self.DEGREES_F,
            self.KELVIN]))
        meassuered_data.append(meassuered_temps[0])
        meassuered_data.append(meassuered_temps[1])
        meassuered_data.append(meassuered_temps[2])
        return meassuered_data
