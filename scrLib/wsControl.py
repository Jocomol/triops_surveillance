# Imports
from thermo import Thermo
from dbConnector import DBConnector
import pytemperature
import sys
import time




class Controller():  # Controlls everything and manages the weatherstation

    def __init__(self):  # Creates all the Objects
        self.name = "Controller"
        self.thermo = Thermo()
        self.db_connector = DBConnector()

    def main(self):  # Calls all methods and writes results into the database
        data_array = self.thermo.read_measurement(len(sys.argv) >= 2 and sys.argv[1]=="-l")
        self.db_connector.database_insert_measurement(data_array)


if __name__ == "__main__":
    controller = Controller()
    controller.main()
