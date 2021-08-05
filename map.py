import event
import text


UP = ['w', 'W', 'ｗ', 'Ｗ']
DOWN = ['s', 'S', 'ｓ', 'Ｓ']
LEFT = ['a', 'A', 'あ', 'Ａ']
RIGHT = ['d', 'D', 'ｄ', 'Ｄ']
ESC = ['q', 'Q', 'ｑ', 'Ｑ']

MAP = [
    ['0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','P','1','0','1','1','1','1','1','1','1','0'],
    ['0','1','1','0','1','1','1','1','1','1','1','0'],
    ['0','1','1','0','1','1','0','1','1','1','1','0'],
    ['0','1','1','0','1','1','0','1','1','1','1','0'],
    ['0','1','1','1','1','1','0','1','1','1','1','0'],
    ['0','1','1','1','1','1','0','1','1','1','G','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0'],
]


HP_FORMAT = ' HP:[{}/{}] '


class Map():
    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

    @property
    def now_h(self):
        return self._now_h

    @now_h.setter
    def now_h(self, value):
        self._now_h = value

    @property
    def now_w(self):
        return self._now_w

    @now_w.setter
    def now_w(self, value):
        self._now_w = value

    @property
    def goal_flg(self):
        return self._goal_flg

    @goal_flg.setter
    def goal_flg(self, value):
        self._goal_flg = value

    @property
    def game_over_flg(self):
        return self._game_over_flg

    @game_over_flg.setter
    def game_over_flg(self, value):
        self._game_over_flg = value

    def __init__(self):
        self._now_h = 1
        self._now_w = 1
        self._counter = 0
        self._goal_flg = False
        self._game_over_flg = False

    def show(self):
        event.clear()
        print(text.MES_HOW_TO_PLAY)
        for array in MAP:
            map = ''
            for i in array:
                if i == '0':
                    map = map + '＃'
                if i == '1':
                    map = map + '　'
                if i == 'P':
                    map = map + 'P '
                if i == 'G':
                    map = map + 'G '
            print(map)

    def move(self):
        while True:
            input_key = input()

            # 終了
            if input_key in ESC:
                self.game_over_flg = True
                break

            # 下へ
            if input_key in DOWN:
                if MAP[self.now_h +1][self.now_w] == 'G':
                    self.goal_flg = True
                    break
                if  MAP[self.now_h +1][self.now_w] == '1':
                    MAP[self.now_h +1][self.now_w] = 'P'
                    MAP[self.now_h][self.now_w] = '1'
                    self.now_h += 1
                else:
                    print(text.MES_CAN_NOT_MOVE)
                    continue

            # 左へ 
            elif input_key in LEFT:
                if MAP[self.now_h][self.now_w -1] == 'G':
                    self.goal_flg = True
                    break
                if MAP[self.now_h][self.now_w -1] == '1':
                    MAP[self.now_h][self.now_w -1] = 'P'
                    MAP[self.now_h][self.now_w] = '1'
                    self.now_w -= 1
                else:
                    print(text.MES_CAN_NOT_MOVE)
                    continue

            # 右へ
            elif input_key in RIGHT:
                if MAP[self.now_h][self.now_w +1] == 'G':
                    self.goal_flg = True
                    break
                if MAP[self.now_h][self.now_w +1] == '1':
                    MAP[self.now_h][self.now_w +1] = 'P'
                    MAP[self.now_h][self.now_w] = '1'
                    self.now_w += 1
                else:
                    print(text.MES_CAN_NOT_MOVE)
                    continue

            # 上へ
            elif input_key in UP:
                if MAP[self.now_h -1][self.now_w] == 'G':
                    self.goal_flg = True
                    break
                if MAP[self.now_h -1][self.now_w] == '1':
                    MAP[self.now_h -1][self.now_w] = 'P'
                    MAP[self.now_h][self.now_w] = '1'
                    self.now_h -= 1
                else:
                    print(text.MES_CAN_NOT_MOVE)
                    continue

            # 不正な入力の場合
            else:
                print(text.MES_CAN_NOT_USE_KEY)
                continue

            self.counter += 1
            break
