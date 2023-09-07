class Mode:
    """モード
    """
    START = 1
    FIELD = 150
    ITEM_LIST = 200
    STATUS = 300
    HELP = 301
    BUTTLE = 400
    ESCAPE = 500
    GAME_CLEAR = 600
    GAME_OVER = 601


class FieldAction:
    NOTHING = 1
    MOVE = 100
    CHANGE = 200


class ButtleAction:
    NOTHING = 1
    MOVE = 100
    DECISION = 200
    CHANGE = 300


class ItemListAction:
    NOTHING = 1
    MOVE = 100
    DECISION = 200
    ESCAPE = 300
