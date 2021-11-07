from enum import Enum


class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    END = '\033[0m'


class Item(str, Enum):

    """マップアイテム一覧
    """
    def __new__(cls, value, map_item, title, description, recovery):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.map_item = map_item
        obj.title = title
        obj.description = description
        obj.recovery = recovery
        return obj

    BLOCK = 'B01', Color.GREEN + '＃' + Color.END, '壁', '侵入不可エリア（壁）', 0
    EMPTY = 'E01', '　', '空地', '何もないフィールド', 0
    PLAYER = 'P01', Color.RED + 'P ' + Color.END, 'プレイヤー', 'プレイヤーの現在位置', 0
    GOAL = 'G01', 'G ', 'ゴール', 'ゴールの位置', 0
    WEAPON = 'W01', '剣', '勇者の剣', '武器/勇者の剣/持っているだけで攻撃力アップ：', 0
    SIELD = 'S01', '盾', '勇者の盾', '防具/勇者の盾/持っているだけで防御力アップ', 0
    HERBS = 'H01', '薬', '薬草', '[薬草]使うとHPがすこし回復する', 100
    POTION = 'H02', '薬', 'ポーション', '[ポーション]使うとHPが回復する', 200
    ELIXIR = 'H10', '薬', 'エリクサー', '[エリクサー]使うとHPが全回復する', 9999
