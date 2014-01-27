class Move(object):

    def __init__(self):
        self.id = 0
        self.white = ''
        self.white_comment = ''
        self.black = ''
        self.black_comment = ''

    def dump(self):
        return '{}. {} {}'.format(self.id, self.white, self.black)




