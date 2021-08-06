from random import randint

from event import Event
from text import Text


ATTACK = ['あ', 'a']
MAGIC = ['ｓ', 's']
ESCAPE = ['ｄ', 'd']


class Buttle():
    @property
    def appear_flg(self):
        return self._appear_flg

    @appear_flg.setter
    def appear_flg(self, value):
        self._appear_flg = value

    def __init__(self):
        self._appear_flg = False

    def buttle(self, player, monster):
        self.appear_flg = True

        while True:
            # 初期画面表示
            Event.clear()
            print(Text.MES_HOW_TO_BUTTLE)
            print(Text.PLAYER_STATUS.format(
                player.name, player.hp, player.max_hp, player.mp, player.max_mp
            ))
            print(Text.MONSTER_STATUS.format(monster.name, monster.hp))
            
            # モンスターのHPが０以下の場合
            if monster.hp <= 0:
                input(Text.KNOCK_OUT_MONSTER.format(monster.name))
                input(Text.MES_GET_EXP.format(monster.level))
                player.exp += monster.level

                # レベルの二乗より経験値が大きい場合
                if player.level**2 <= player.exp:
                    player.level_up()
                    input(Text.MES_LEVEL_UP.format(player.name, player.level))
                break

            # プレイヤーのHPが０以下の場合
            if player.hp <= 0:
                input(Text.KNOCK_OUT_PLAYER.format(player.name))
                break

            # モンスター登場
            if self.appear_flg:
                input(Text.MES_APPEAR_MONSTER.format(monster.name))
                self.appear_flg = False

            # プレイヤー入力待ち
            input_key = input(Text.MES_CHOOSE_ACTION)

            # こうげきの場合
            if input_key in ATTACK:

                # プレイヤーの攻撃
                input(Text.MES_ATTACK_FROM_PLAYER.format(player.name))
                damage = player.power + randint(0, player.level)
                input(Text.MES_DAMAGE.format(damage))
                monster.hp -= damage

            # まほうの場合
            elif input_key in MAGIC:
                input(Text.MES_MAGIC.format(player.name))
                if player.mp > 0:
                    player.mp -= 1
                    damage = 100 + player.level * 10
                    monster.hp -= damage
                    input(Text.MES_DAMAGE.format(damage))
                else:
                    input(Text.MES_MP_IS_EMPTY)

            # にげるの場合
            elif input_key in ESCAPE:
                escape = randint(1, 100)
                if escape >= 30:
                    input(Text.MES_ESCAPE)
                    break
                else:
                    input(Text.MES_CAN_NOT_ESCAPE)

            # 未入力の場合
            elif input_key == '':
                continue

            # 無効なキーの場合
            else:
                input(Text.MES_CAN_NOT_USE_KEY)
                continue

            # 攻撃によってモンスターのHPが0以下になった場合
            if monster.hp <= 0:
                continue

            # モンスターの攻撃
            input(Text.MES_ATTACK_FROM_MONSTER.format(monster.name))
            damage = monster.power + randint(0, monster.level) - player.defense
            if damage < 0:
                damage = 0
            player.hp -= damage
            input(Text.MES_DAMAGE.format(damage))