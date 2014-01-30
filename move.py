import re

class Move(object):

    def __init__(self):
        self.id = 0
        self.white = ''
        self.white_comment = ''
        self.black = ''
        self.black_comment = ''

    def dump(self):
        return '{}. {} {}'.format(self.id, self.white, self.black)

    def validate_format(self, str_move):
        return re.match('^\d+\.+\s*.*', str_move)

    def parse(self, str_move):
        if self.validate_format(str_move):
            return "ERROR" # should raise an error here








