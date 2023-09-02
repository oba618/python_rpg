from abc import ABC, abstractmethod

from src.utils.const import (
    ButtleAction,
    FieldAction,
    ItemListAction,
    Mode,
)


class InputKey(ABC):
    """入力キー抽象クラス
    """

    @abstractmethod
    def __init__(self):
        self.field_action = FieldAction.NOTHING
        self.item_list_action = ItemListAction.NOTHING
        self.buttle_action = ButtleAction.NOTHING

    @abstractmethod
    def move_map(self) -> list:
        """マップのプレイヤーを移動させる

        Returns:
            list: _description_
        """
        pass

    @abstractmethod
    def move_cursor(self) -> int:
        """カーソルを移動させる

        Returns:
            int: _description_
        """
        pass

    @abstractmethod
    def change_display(self) -> Mode:
        """モードを変更させる

        Returns:
            Mode: モード
        """
        pass


class InputKeyUp(InputKey):

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
        self.field_action = FieldAction.NOTHING
        self.item_list_action = ItemListAction.DECISION
        self.buttle_action = ButtleAction.DECISION

    def move_map(self):
        pass

    def move_cursor(self):
        pass

    def change_display(self):
        pass
