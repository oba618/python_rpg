class Monster():
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

    def __init__(self, counter):
        self._name = self.select_name(counter)
        self._hp = 10 + counter

    @staticmethod
    def select_name(counter):
        if 0 <= counter < 10:
            return 'スライム'
        elif 10 <= counter < 20:
            return 'ゴブリン'
        elif 20 <= counter < 30:
            return 'ゴーレム'
        else:
            return 'ドラゴン'
