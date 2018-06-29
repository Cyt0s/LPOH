class input_format(object):
    def __init__(self,sign='Cy>>'):
        self.__sign = sign
        
    def ask_for_command(self):
        return raw_input(self.__sign)