from event import Event
from random import randint
from text import Text


class Monster:

    # モンスター名
    SLIME = 'スライム'
    GOBLINS = 'ゴブリン'
    GOLEM = 'ゴーレム'
    DRAGON = 'ドラゴン'

    def __init__(self, counter):

        self.appear_flg = True
        self.action_flg = False

        # モンスター作成
        (
            self.name,
            self.hp,
            self.power,
            self.level,
        ) = self.create_monster(counter)

    def create_monster(self, counter: int) -> tuple:
        """モンスター作成

        Args:
            counter (int): [description]

        Returns:
            tupple: 各ステータス
        """

        # スライム作成
        if 0 <= counter < 30:
            hp = 20 + randint(1, 3)
            power = 10 + randint(1, 3)
            level = 1

            return (self.SLIME, hp, power, level)

        # ゴブリン作成
        elif 30 <= counter < 60:
            hp = 50 + randint(10, 15)
            power = 20 + randint(5, 10)
            level = 2

            return (self.GOBLINS, hp, power, level)

        # ゴーレム作成
        elif 60 <= counter < 90:
            hp = 100 + randint(20, 30)
            power = 30 + randint(10, 20)
            level = 5

            return (self.GOLEM, hp, power, level)

        # ドラゴン作成
        else:
            hp = 200 + randint(50, 100)
            power = 50 + randint(30, 40)
            level = 10

            return (self.DRAGON, hp, power, level)

    def appear(self):
        """モンスター登場
        """
        print(Text.MES_APPEAR_MONSTER.format(self.name))
        Event.input()

    def attack(self, player):
        """モンスターの攻撃

        Args:
            player (Player): プレイヤー
        """

        input(Text.MES_ATTACK_FROM_MONSTER.format(self.name))

        # ダメージ量
        damage = self.power + randint(0, self.level) - player.defense
        if damage < 0:
            damage = 0

        # プレイヤーにダメージ
        player.hp -= damage
        input(Text.MES_DAMAGE.format(damage))

        self.action_flg = False

    def knock_out(self):
        """モンスターノックアウト
        """
        print(Text.KNOCK_OUT_MONSTER.format(self.name))
        Event.input()
