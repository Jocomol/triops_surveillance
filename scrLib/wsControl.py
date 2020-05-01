# Imports
from thermo import Thermo
from dbConnector import DBConnector
import pytemperature
import logging


class Controller():  # Controlls everything and manages the weatherstation

    def __init__(self):  # Creates all the Objects
        self.name = "Controller"
        self.thermo = Thermo()
        self.db_connector = DBConnector()
        self.controller_logger.info("All Objects created")

    def main(self):  # Calls all methods and writes results into the database
        data_array = self.thermo.read_measurement()
        self.db_connector.database_insert_measurement(data_array)


if __name__ == "__main__":
    controller = Controller()
    controller.main()
