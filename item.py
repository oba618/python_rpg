from enum import Enum


class Item(str, Enum):

    """マップアイテム一覧
    """
    def __new__(cls, value, map_item, title, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.map_item = map_item
        obj.title = title
        obj.description = description
        return obj

    BLOCK = 'B', '＃', '壁', '侵入不可エリア（壁）'
    EMPTY = 'E', '　', '空地', '何もないフィールド'
    PLAYER = 'P', 'P ', 'プレイヤー', 'プレイヤーの現在位置'
    GOAL = 'G', 'G ', 'ゴール', 'ゴールの位置'
    WEAPON = 'W', '剣', '勇者の剣', '武器/勇者の剣/持っているだけで攻撃力アップ：'
    SIELD = 'S', '盾', '勇者の盾', '防具/勇者の盾/持っているだけで防御力アップ'
    HERBS = 'H', '薬', '薬草', '道具/薬草/使うとHPがすこし回復する'
