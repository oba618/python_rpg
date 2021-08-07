from event import Event
from text import Text
from map import MapItem


KEY_LIST = {
    'close': ['e', 'E', 'え', 'E'],
    'up': ['w', 'W', 'ｗ', 'Ｗ'],
    'down': ['s', 'S', 'ｓ', 'Ｓ'],
    'use': ['x', 'X', 'ｘ', 'Ｘ'],
}


class Player():

    PLAYER_INITIAL_HP = 200
    PLAYER_INITIAL_MP = 5
    PLAYER_INITIAL_POWER = 10
    PLAYER_INITIAL_DEFENSE = 0
    PLAYER_INITIAL_EXP = 0
    PLAYER_INITIAL_LEVEL = 1
    PLAYER_INITIAL_ITEM_LIST = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def max_hp(self):
        return self._max_hp

    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def max_mp(self):
        return self._max_mp

    @max_mp.setter
    def max_mp(self, value):
        self._max_mp = value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        self._item_list = value

    def __init__(self, name):
        self._name = name
        self._max_hp = self.PLAYER_INITIAL_HP
        self._hp = self.PLAYER_INITIAL_HP
        self.max_mp = self.PLAYER_INITIAL_MP
        self._mp = self.PLAYER_INITIAL_MP
        self._power = self.PLAYER_INITIAL_POWER
        self._defense = self.PLAYER_INITIAL_DEFENSE
        self._exp = self.PLAYER_INITIAL_EXP
        self._level = self.PLAYER_INITIAL_LEVEL
        self._item_list = self.PLAYER_INITIAL_ITEM_LIST

    def level_up(self):
        self.max_hp += 20
        self.power += 5
        self.defense += 1
        self.level += 1

    def get_item(self, field):
        # 剣の場合
        if field == MapItem.WEAPON.value:
            self.power += 30
            input(Text.MES_GET_WEAPON)

        # 盾の場合
        if field == MapItem.SIELD.value:
            self.defense += 10
            input(Text.MES_GET_SIELD)

        # 薬の場合
        if field == MapItem.HERBS.value:
            input(Text.MES_GET_HERBS)

        # アイテム一覧に詰める
        self.item_list.append(MapItem(field))

    def show_item_list(self):
        """アイテム一覧を表示
        """
        select_index = 0

        while True:
            Event.clear()
            print(Text.HOW_TO_USE_ITEM)
            print(Text.ITEM_LIST)

            # アイテムがある場合
            if self.item_list:
                for index, item in enumerate(self.item_list):

                    # 選択中のアイテムの場合
                    if index == select_index:
                        print('[＊]' + item.title)
                    else:
                        print('[　]' + item.title)

            # アイテムがない場合
            else:
                print(Text.NOTING_ITEM)
            print(Text.ITEM_LIST_END)

            # キー入力待ち
            input_key = input()

            # CLOSEの場合
            if input_key in KEY_LIST['close']:
                break

            # UPの場合
            elif input_key in KEY_LIST['up']:
                select_index = select_index - 1 \
                    if select_index > 0 else 0

            # DOWNの場合
            elif input_key in KEY_LIST['down']:
                select_index = select_index + 1 \
                    if select_index < len(self.item_list) - 1 else select_index

            # USEの場合
            elif input_key in KEY_LIST['use']:
                item_object = self.item_list[select_index]
                answer = input(Text.USE_ITEM_CONFIRM.format(
                    item_object.description))

                # Yesの場合
                if Event.is_yes(answer):
                    if item_object == MapItem.HERBS:
                        self.hp += 100
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        self.item_list.pop(select_index)
                        select_index = 0
                        input(Text.MES_USE_HERB)
                    else:
                        input(Text.MES_USE_EQUIPMENT)

            else:
                break
