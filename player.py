from text import Text
from map import MapItem


class Player():
    
    PLAYER_INITIAL_HP = 200
    PLAYER_INITIAL_MP = 5
    PLAYER_INITIAL_POWER = 10
    PLAYER_INITIAL_DEFENSE = 0
    PLAYER_INITIAL_EXP = 0
    PLAYER_INITIAL_LEVEL = 1

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
            self.hp += 50
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            input(Text.MES_GET_HERBS)
