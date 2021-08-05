import text
import event


ATTACK = ['1', '１']
MAGIC = ['2', '２']
ESCAPE = ['3', '３']


class Buttle():
    def __init__(self):
        pass
    
    @staticmethod
    def buttle(player, monster):
        while True:
            event.clear()
            print(text.PLAYER_STATUS.format(player.name, player.hp, player.max_hp))
            print(text.MES_APPEAR_MONSTER.format(monster.name))
            print(text.MES_HOW_TO_BUTTLE)
            input_key = input()

            # こうげきの場合
            if input_key in ATTACK:
                input(text.MES_ATTACK.format(player.name))
                monster.hp = 0
                print(text.MONSTER_STATUS.format(monster.name, monster.hp))

            # まほうの場合
            elif input_key in MAGIC:
                input(text.MES_MAGIC.format(player.name))
                monster.hp = 0
                print(text.MONSTER_STATUS.format(monster.name, monster.hp))
                break

            # にげるの場合
            elif input_key in ESCAPE:
                input(text.MES_ESCAPE)
                break

            # 無効なキーの場合
            else:
                input(text.MES_CAN_NOT_USE_KEY)
                continue

            # モンスターのHPが０以下の場合
            if monster.hp <= 0:
                input(text.KNOCK_OUT_MONSTER.format(monster.name))
                break

            # プレイヤーのHPが０以下の場合
            if player.hp <= 0:
                input(text.KNOCK_OUT_PLAYER.format(player.name))
                break