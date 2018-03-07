
from numpy import *

# import curses
# stdscr = curses.initscr()

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::-1] for row in field]


field1 = [[2,2,0],[2,2,0],[0,0,0]]

field2 = [[1,2,1],[0,0,2],[0,0,0]]

a = transpose(field1)

b = invert(field1)


def move_row_left(row):
    def tighten(row):  # squeese non-zero elements together
        new_row = [i for i in row if i != 0]
        new_row += [0 for i in range(len(row) - len(new_row))]
        return new_row

    def merge(row):
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.append(2 * row[i])
                # self.score += 2 * row[i]
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                    new_row.append(0)
                else:
                    new_row.append(row[i])
        assert len(new_row) == len(row)
        return new_row

    return tighten(merge(tighten(row)))


moves = {}
moves['Left'] = lambda field: \
    [move_row_left(row) for row in field]
moves['Right'] = lambda field: \
    invert(moves['Left'](invert(field)))
moves['Up'] = lambda field: \
    transpose(moves['Left'](transpose(field)))
moves['Down'] = lambda field: \
    transpose(moves['Right'](transpose(field)))

print(a)
print(b)
#
# print(c)
print(moves['Left'](field1))
print(moves['Up'](field1))

line = '+' + ('+------' * 4 + '+')[1:]

line2 = 'dfdafasdfadfadsf'[1:8]

print(line)
print(line2)


# def init():
#     aa = 90
#     return aa
state_actions = {
            'Init': 'init',}
print(state_actions['Init'])
#
# def get_user_action(keyboard):
#     char = "N"
#     while char not in actions_dict:
#         char = keyboard.getch()
#     return actions_dict[char]
#
# get_user_action(stdscr)
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actionsss = ['1','2','3','4','5','6']
directary = dict(zip(actions,actionsss))
print(directary)