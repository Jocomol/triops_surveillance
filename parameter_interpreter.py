class ParameterInterpreter():

    def __init__(self):
        self.lights = False
        self.message = False
        self.temperatur = True
        self.short = True

    def interpret(self, arguments):
        for argument in arguments:
            if argument == "-l":
                self.lights = True
            elif argument == "-m":
                self.message = True
            elif argument == "-t":
                self.short = True
            else:
                pass
