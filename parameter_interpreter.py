class ParameterInterpreter():

    def __init__(self):
        self.lights = False
        self.message = False

    def interpret(self, arguments):
        for argument in arguments:
            if argument == "-l":
                self.lights = True
            elif argument == "-m":
                self.message = True
            else:
                pass
