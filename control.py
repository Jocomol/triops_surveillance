#!/usr/bin/env python3
from thermo import Thermo
from dbConnector import DBConnector
from notificationSender import PushoverSender
import sys


class Controller():  # Starts eveything

    def __init__(self):  # Creates all the Objects
        self.name = "Controller"
        self.thermo = Thermo()
        self.db_connector = DBConnector()
        self.pushoverSender = PushoverSender("umudoepm93f2g8c5489aig8tr2i31c","ayzgokayp6qypch2qw6es4pc2usjto")

    def main(self):  # Calls all methods and writes results into the database
        data_array = self.thermo.read_measurement()
        self.db_connector.database_insert_measurement(data_array)

        if data_array[1] < 23:
            color = "blue"
            message = "Das Triopsgehege ist unter 23 Grad, sofort die Lampe näherrücken."
        elif data_array[1] > 23 and data_array[1] <= 24:
            color = "aqua"
            message = "Das Triopsgehege ist zwischen 23 und 24 Grad, bitte die Lampe näherrücken."
        elif data_array[1] > 24 and data_array[1] <= 26:
            color = "green"
        elif data_array[1] > 26 and data_array[1] <= 27:
            color = "orange"
            message = "Das Triopsgehege ist zwischen 26 und 27 Grad, bitte die Lampe wegrücken."
        elif data_array[1] > 27:
            color = "red"
            message = "Das Triopsgehege ist über 27 Grad, sofort die Lampe wegrücken."
        else:
            color = "purple"
            message = "Beim Messen gab es einen Fehler, bitte nachprüfen."

        if len(sys.argv) >= 2 and sys.argv[1] == "-l":
            bashCommand = "hueadm light 2 " + color + " bri=255"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

        if color != "green":
            self.pushoverSender.send_notification(message)
        print(color)
        print(message)
        print(data_array[1])
if __name__ == "__main__":
    controller = Controller()
    controller.main()