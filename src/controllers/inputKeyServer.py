from src.controllers.key import Key
from src.controllers.inputKey import (
    InputKey,
    InputKeyDecision,
    InputKeyDown,
    InputKeyEnter,
    InputKeyEmpty,
    InputKeyEsc,
    InputKeyHelp,
    InputKeyItem,
    InputKeyLeft,
    InputKeyRight,
    InputKeyStatus,
    InputKeyUp,
)


class InputKeyServer:
    """入力キーのオブジェクトを提供するクラス
    """

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

    @classmethod
    def get_input_key_obj(cls, input_value: str) -> InputKey:
        """キーオブジェクト取得

        Args:
            input_value (str): 標準入力された値

        Returns:
            InputKey: 入力キークラスのインスタンス
        """

        # 入力キークラスを取得
        input_key = cls.input_key_def[input_value]

        # 入力キークラスのインスタンスを返却
        return input_key()
