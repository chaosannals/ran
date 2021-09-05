from time import time_ns

class IdentifierMaker:
    '''
    '''

    def __init__(self, maker_id):
        '''
        '''

        self.maker_id = maker_id
        self.last_id = 0
        self.last_at = time_ns() >> 20

    def make(self):
        '''
        '''

        result = self.maker_id << (41 + 12)
        now = time_ns() >> 20
        if now == self.last_at:
            self.last_id += 1
        else:
            self.last_id = 0
            self.last_at = now
        return result | (now << 12) | self.last_id