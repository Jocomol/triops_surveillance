
import os
import sys
from w1thermsensor import W1ThermSensor
import datetime
import subprocess


class Thermo(W1ThermSensor):

    def __init__(self):
        W1ThermSensor.__init__(
            self,
            W1ThermSensor.THERM_SENSOR_DS18B20,
            "00000833e8ff")  # TODO

    def read_measurement(self, lamps):
        meassuered_data = [str(datetime.datetime.now().isoformat())]
        meassuered_temps = (self.get_temperatures([
            self.DEGREES_C,
            self.DEGREES_F,
            self.KELVIN]))
        meassuered_data.append(meassuered_temps[0])
        meassuered_data.append(meassuered_temps[1])
        meassuered_data.append(meassuered_temps[2])
        if lamps:
            ## TODO
            if measurement_temps[0] < 23:
                color = "blue"
            elif measurement_temps[0] > 23 and measurement_temps[0] <= 24:
                color = "aqua"
            elif measurement_temps[0] > 24 and measurement_temps[0] <= 26:
                color="green"
            elif measurement_temps[0] > 26 and measurement_temps[0] <= 27:
                color="orange"
            elif measurement_temps[0] > 27:
                color="red"
            else:
                color="purple"

            bashCommand = "hueadm light 2 " + color + " bri=255"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        return meassuered_data
