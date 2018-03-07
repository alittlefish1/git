from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self,num_side = 6):
        """骰子默认为6面"""
        self.num_side = num_side

    def roll(self):
        """掷骰子的方法"""
        return randint(1,self.num_side)