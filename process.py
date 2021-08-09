import sys

from event import Event
from text import Text


class Process:
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'
    ESC = 'q'
    ITEM = 'e'
    STATUS = 'z'
    DECISION = 'x'
    HELP = 'c'
    EMPTY = ''
    KEY_LIST = {
        UP: ['w', 'W', 'ｗ', 'Ｗ'],
        DOWN: ['s', 'S', 'ｓ', 'Ｓ'],
        LEFT: ['a', 'A', 'あ', 'Ａ'],
        RIGHT: ['d', 'D', 'ｄ', 'Ｄ'],
        ESC: ['q', 'Q', 'ｑ', 'Ｑ'],
        ITEM: ['e', 'E', 'え', 'E'],
        STATUS: ['z', 'Z', 'ｚ', 'Ｚ'],
        DECISION: ['x', 'X', 'ｘ', 'Ｘ'],
        HELP: ['c', 'C', 'ｃ', 'Ｃ'],
        EMPTY: ['', ' ', '　'],
    }

    @staticmethod
    def show_title():
        # タイトル画面を表示
        print(Text.TITLE)

    @staticmethod
    def input_player_name():
        # プレイヤーの名前を入力
        player_name = ''
        while not player_name:
            Event.clear()
            print(Text.MES_INPUT_PLAYER_NAME)
            player_name = Event.input()

            # プレイヤー名が長い場合
            if len(player_name) >= Text.PLAYER_NAME_MAX_LENGTH:
                input(Text.MES_PLAYER_NAME_IS_TOO_LONG)
                player_name = ''
                continue

            # プレイヤー名が未入力の場合
            if len(player_name) == 0:
                continue

        return player_name

    @staticmethod
    def confirm_input_player_name(player_name):
        # プレイヤーの応答がYesか否か
        print(Text.QUESTION_ANSWER.format(player_name))
        player_name_answer = Event.input()
        if Event.is_yes(player_name_answer):
            return player_name
        else:
            player_name = ''
            Event.clear()

    @classmethod
    def input_player_key(cls):
        input_key = ''
        while not input_key:
            input_key = Event.input()
            for key, value in cls.KEY_LIST.items():
                if input_key in value:
                    return key

            # 不正な入力の場合
            else:
                input_key = ''
                print(Text.MES_CAN_NOT_USE_KEY)

    def show_player_status(player):
        required_exp = player.level**2 - player.exp

        Event.clear()
        print(Text.MES_HOW_TO_PLAY)
        print(Text.PLAYER_STATUS.format(
            player.name, player.hp, player.max_hp, player.mp, player.max_mp
        ))
        print(Text.PLAYER_STATUS_DETAIL.format(
            player.level, player.exp, required_exp, player.power, player.defense
        ))
        Event.input()
        return
