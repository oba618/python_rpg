from random import randint


class Monster:
    SLIME = 'スライム'
    GOBLINS = 'ゴブリン'
    GOLEM = 'ゴーレム'
    DRAGON = 'ドラゴン'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def __init__(self, counter):
        self._name, self._hp, self._power, self._level = \
            self.create_monster(counter)

    def create_monster(self, counter):
        # スライム作成
        if 0 <= counter < 20:
            hp = 20 + randint(1, 3)
            power = 10 + randint(1, 3)
            level = 1
            return (self.SLIME, hp, power, level)

        # ゴブリン作成
        elif 20 <= counter < 40:
            hp = 50 + randint(10, 15)
            power = 20 + randint(5, 10)
            level = 2
            return (self.GOBLINS, hp, power, level)

        # ゴーレム作成
        elif 40 <= counter < 60:
            hp = 100 + randint(20, 30)
            power = 30 + randint(10, 20)
            level = 3
            return (self.GOLEM, hp, power, level)

        # ドラゴン作成
        else:
            hp = 200 + randint(50, 100)
            power = 50 + randint(30, 40)
            level = 4
            return (self.DRAGON, hp, power, level)
