class ParameterInterpreter():

    def __init__(self):
        self.lights = False
        self.message = False
        self.temperature = False
        self.short = False
        self.debug = False

    def interpret(self, arguments):
        for argument in arguments:
            if argument == "-l":
                self.lights = True
            elif argument == "-m":
                self.message = True
            elif argument == "-s":
                self.short = True
            elif argument == "-t":
                self.temperature = True
            elif argument == "-d":
                self.debug = True

            else:
                pass
