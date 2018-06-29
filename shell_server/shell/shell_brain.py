class ShellBrain(object):
    def __init__(self,input_format,output_format):
        self.__input_format = input_format
        self.__output_format = output_format
        

    def start(self):
        stop_command = False
        while stop_command != True:
            input_command = self.__input_format.ask_for_command()
            self.__output_format.print_data(input_command)
            
