class ParameterInterpreter():

    def __init__(self):
        self.lights = False
        self.silent = False

    def interpret(self, arguments):
        for argument in arguments:
            if argument == "-l":
                self.lights = True
            elif argument == "-m":
                self.silent = True
            else:
                pass
