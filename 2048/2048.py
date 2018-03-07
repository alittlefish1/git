import curses
from random import randrange,choice
from collections import defaultdict



def main(stdscr):
    def init():
        #初始话棋盘
        return 'Game'

    def not_game(state):
        #画出Gameover后者是win的画面
        #读取用户输入的action，来判断是否是重启还是结束游戏
        responses = defaultdict(lambda :state)#默认值是当前状态，没有其他的行为会一直在当前界面循环
        responses['Restart'],responses['Exit'] = 'Init','Exit'
        return resqonses[action]
    def game():
        #画出当前棋盘状态
        #读取用户输出的到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步：
            if 胜利了：
                return 'Win'
            if 游戏失败了：
                return 'Gameover'
        return 'Game'

    state_action = {
        'Init':init,
        'Win': lambda :not_game('Win'),
        'Gameover': lambda : not_game('Gameover'),
        'Game':game
    }

    state = 'Init'

    #状态机开始循环
    while state != 'Eixt':
        state = state_actions[state]()
def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]




class GameField():
    '''创造棋盘'''
    def __init__(self,height = 4,width = 4,win = 2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0 #当前分数
        self.highscore = 0 #最高分
        self.reset()
