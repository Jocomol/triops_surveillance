class ParameterInterpreter():

    self.lights = False
    self.silent = False

    def interpret(arguments):
        for argument in arguments:
            if argument == "-l":
                self.lights = True
            elif argument == "-m":
                self.silent = True
            else:
                pass
