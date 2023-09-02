from abc import ABC, abstractmethod

from src.utils.const import (
    ButtleAction,
    FieldAction,
    ItemListAction,
    Mode,
)


"""
キー入力に応じた十字キークラス群
十字キー -> 上下左右の入力を受け付けるキー

基底クラス: InputKey

サーバクラス: InputKeyServer -> キー入力に応じたInputKeyクラスを呼び出す

メソッド:
    move_map() -> 移動させる
    move_cursor() -> カーソルを移動させる
"""


class Key:

    # キー名
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
    ENTER = '\r'
    KEY_LIST = {
        UP: ['w', 'W', 'ｗ', 'Ｗ'],
        DOWN: ['s', 'S', 'ｓ', 'Ｓ'],
        LEFT: ['a', 'A', 'あ', 'Ａ'],
        RIGHT: ['d', 'D', 'ｄ', 'Ｄ'],
        ESC: ['q', 'Q', 'ｑ', 'Ｑ'],
        ITEM: ['e', 'E', 'え', 'Ｅ'],
        STATUS: ['z', 'Z', 'ｚ', 'Ｚ'],
        DECISION: ['x', 'X', 'ｘ', 'Ｘ'],
        HELP: ['c', 'C', 'ｃ', 'Ｃ'],
        EMPTY: ['', ' ', '　'],
        ENTER: ['\r']
    }
    MOVE_KEY_LIST = [
        UP, DOWN, LEFT, RIGHT,
    ]


class InputKey(ABC):

    @abstractmethod
    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.NOTHING
        self.item_list_action = ItemListAction.NOTHING
        self.buttle_action = ButtleAction.NOTHING

    @abstractmethod
    def move_map(self) -> list:
        pass

    @abstractmethod
    def move_cursor(self) -> int:
        pass

    @abstractmethod
    def change_display(self) -> Mode:
        pass


class InputKeyUp(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.MOVE
        self.item_list_action = ItemListAction.MOVE
        self.buttle_action = ButtleAction.MOVE

    def move_map(self):
        return [-1, 0]

    def move_cursor(self, list_len, select_index):
        return select_index - 1 \
            if select_index > 0 \
            else list_len - 1

    def change_display(self):
        pass


class InputKeyDown(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.MOVE
        self.item_list_action = ItemListAction.MOVE
        self.buttle_action = ButtleAction.MOVE

    def move_map(self):
        return [1, 0]

    def move_cursor(self, list_len, select_index):
        return select_index + 1 \
            if select_index < list_len - 1 \
            else 0

    def change_display(self):
        pass


class InputKeyLeft(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.MOVE
        self.item_list_action = ItemListAction.ESCAPE
        self.buttle_action = ButtleAction.NOTHING

    def move_map(self):
        return [0, -1]

    def move_cursor(self):
        pass

    def change_display(self):
        pass


class InputKeyRight(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.MOVE
        self.item_list_action = ItemListAction.ESCAPE
        self.buttle_action = ButtleAction.NOTHING

    def move_map(self):
        return [0, 1]

    def move_cursor(self):
        pass

    def change_display(self):
        pass


class InputKeyEsc(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.CHANGE
        self.item_list_action = ItemListAction.ESCAPE
        self.buttle_action = ButtleAction.CHANGE

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        return Mode.ESCAPE


class InputKeyItem(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.CHANGE
        self.item_list_action = ItemListAction.ESCAPE
        self.buttle_action = ButtleAction.CHANGE

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        return Mode.ITEM_LIST


class InputKeyStatus(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.CHANGE
        self.item_list_action = ItemListAction.ESCAPE
        self.buttle_action = ButtleAction.CHANGE

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        return Mode.STATUS


class InputKeyDecision(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.NOTHING
        self.item_list_action = ItemListAction.DECISION
        self.buttle_action = ButtleAction.DECISION

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        pass


class InputKeyHelp(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.CHANGE
        self.item_list_action = ItemListAction.ESCAPE
        self.buttle_action = ButtleAction.CHANGE

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        return Mode.HELP


class InputKeyEmpty(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.NOTHING
        self.item_list_action = ItemListAction.DECISION
        self.buttle_action = ButtleAction.DECISION

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        pass


class InputKeyEnter(InputKey):

    def __init__(self, value):
        self.value = value
        self.field_action = FieldAction.NOTHING
        self.item_list_action = ItemListAction.DECISION
        self.buttle_action = ButtleAction.DECISION

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        pass


input_key_def = {
    Key.UP: InputKeyUp,
    Key.DOWN: InputKeyDown,
    Key.LEFT: InputKeyLeft,
    Key.RIGHT: InputKeyRight,
    Key.ESC: InputKeyEsc,
    Key.ITEM: InputKeyItem,
    Key.STATUS: InputKeyStatus,
    Key.DECISION: InputKeyDecision,
    Key.HELP: InputKeyHelp,
    Key.EMPTY: InputKeyEmpty,
    Key.ENTER: InputKeyEnter,
}


def get_input_key_obj(input_key: str) -> InputKey:
    """キーオブジェクト取得

    Args:
        input_key (str): 標準入力されたキー

    Returns:
        InputKey: キーオブジェクト
    """

    # オブジェクト取得
    obj = input_key_def[input_key]

    return obj(input_key)
