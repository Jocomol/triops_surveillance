#!/usr/bin/env python3
from thermo import Thermo
from dbConnector import DBConnector
from parameter_interpreter import ParameterInterpreter
import telegram
import subprocess
import sys


class Controller():  # Starts eveything

    def __init__(self):  # Creates all the Objects
        self.name = "Controller"
        self.thermo = Thermo()
        self.db_connector = DBConnector()
        self.parameterInterpreter = ParameterInterpreter()
        self.bot = telegram.Bot('1263907628:AAGJsEeBJmOKzbR3xYuuDolNPXXbsbYyWhY')
        self.chat_id = self.bot.get_updates()[-1].message.chat_id

    def main(self):  # Calls all methods and writes results into the database
        data_array = self.thermo.read_measurement()
        self.db_connector.database_insert_measurement(data_array)
        self.parameterInterpreter.interpret(sys.argv)
        if data_array[1] < 23:
            color = "blue"
            message = "Das Triopsgehege ist unter 23 Grad, sofort die Lampe näherrücken."
        elif data_array[1] > 23 and data_array[1] <= 24:
            color = "aqua"
            message = "Das Triopsgehege ist zwischen 23 und 24 Grad, bitte die Lampe näherrücken."
        elif data_array[1] > 24 and data_array[1] <= 26:
            color = "green"
            message = "all ok"
        elif data_array[1] > 26 and data_array[1] <= 27:
            color = "orange"
            message = "Das Triopsgehege ist zwischen 26 und 27 Grad, bitte die Lampe wegrücken."
        elif data_array[1] > 27:
            color = "red"
            message = "Das Triopsgehege ist über 27 Grad, sofort die Lampe wegrücken."
        else:
            color = "purple"
            message = "Beim Messen gab es einen Fehler, bitte nachprüfen."

        if self.parameterInterpreter.temperature:
            print(data_array[1])
        elif self.parameterInterpreter.short:
            print(str(data_array[1]) + "°C")
        else:
            print("")
            print("---")
            print("Farbe: " + color)
            print("Message: " + message)
            print("Temperatur: " + str(data_array[1]) + "°C")
            print("---")

        if self.parameterInterpreter.message:
            if color != "green":
                self.bot.send_message(chat_id=self.chat_id, text=message)
            elif self.parameterInterpreter.debug:
                message = "Debug test: " + str(data_array[1])
                self.bot.send_message(chat_id=self.chat_id, text=message)

        if self.parameterInterpreter.lights:
            if color != "green":
                bashCommand = "hueadm light 2 " + color + " bri=255"
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()

if __name__ == "__main__":
    controller = Controller()
    controller.main()
