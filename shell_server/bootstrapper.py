from shell import input_format,output_format,shell_brain


class BootStrapper(object):
    def __init__(self,config_dict):
        pass

    def bootstrap(self):
        self.shell_brain = shell_brain.ShellBrain(input_format.InputFormat(),output_format.OutputFormat())

    