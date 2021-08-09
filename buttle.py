from map import MapItem
from random import randint

from event import Event
from process import Process
from text import Text


class Buttle:
    ATTACK = 'こうげき'
    MAGIC = 'まほう'
    ITEM = 'アイテム'
    ESCAPE = 'にげる'
    ACTION_LIST = [
        ATTACK,
        MAGIC,
        ITEM,
        ESCAPE,
    ]

    @property
    def appear_flg(self):
        return self._appear_flg

    @appear_flg.setter
    def appear_flg(self, value):
        self._appear_flg = value

    @property
    def select_index(self):
        return self._select_index

    @select_index.setter
    def select_index(self, value):
        self._select_index = value

    def __init__(self):
        self._appear_flg = False
        self._select_index = 0

    def buttle(self, player, monster):
        self.appear_flg = True

        while True:
            # 初期画面表示
            Event.clear()
            print(Text.MES_HOW_TO_PLAY)
            print(Text.PLAYER_STATUS.format(
                player.name, player.hp, player.max_hp, player.mp, player.max_mp
            ))
            print(Text.MONSTER_STATUS.format(monster.name, monster.hp))

            # モンスターのHPが０以下の場合
            if monster.hp <= 0:
                print(Text.KNOCK_OUT_MONSTER.format(monster.name))
                Event.input()

                # 経験値獲得
                player.exp += monster.level
                print(Text.MES_GET_EXP.format(monster.level))
                Event.input()

                # レベルの二乗より経験値が大きい場合、レベルアップ
                if player.level**2 <= player.exp:
                    player.level_up()
                    print(Text.MES_LEVEL_UP.format(player.name, player.level))
                    Event.input()
                break

            # プレイヤーのHPが０以下の場合
            if player.hp <= 0:
                print(Text.KNOCK_OUT_PLAYER.format(player.name))
                Event.input()
                break

            # モンスター登場
            if self.appear_flg:
                self.appear_flg = False
                print(Text.MES_APPEAR_MONSTER.format(monster.name))
                Event.input()
                continue

            # アクションリスト表示
            print(Text.MES_CHOOSE_ACTION)
            for index, action in enumerate(self.ACTION_LIST):
                if self.select_index == index:
                    print(Text.ICON_SELECTED + action)
                else:
                    print(Text.ICON_NOT_SELECTED + action)

            input_key = Process.input_player_key()

            # UPの場合
            if input_key == Process.UP:
                self.select_index = self.select_index - 1 \
                    if self.select_index > 0 else len(self.ACTION_LIST) - 1
                continue

            # DOWNの場合
            elif input_key == Process.DOWN:
                self.select_index = self.select_index + 1 \
                    if self.select_index < len(self.ACTION_LIST) - 1 \
                    else 0
                continue

            # ESCの場合
            elif input_key == Process.ESC:
                continue

            # STATUSの場合
            elif input_key == Process.STATUS:
                continue

            # HELPの場合
            elif input_key == Process.HELP:
                continue

            # ITEMの場合
            elif input_key == Process.ITEM:
                used_item_flg = self.show_item_list(player, monster)
                if not used_item_flg:
                    continue

            # DECESIONの場合、未入力の場合
            elif input_key == Process.DECISION or \
                    input_key == Process.EMPTY:

                # こうげきの場合
                if self.select_index == self.ACTION_LIST.index(self.ATTACK):
                    # プレイヤーの攻撃
                    input(Text.MES_ATTACK_FROM_PLAYER.format(player.name))
                    damage = player.power + randint(0, player.level)
                    input(Text.MES_DAMAGE.format(damage))
                    monster.hp -= damage

                # まほうの場合
                elif self.select_index == self.ACTION_LIST.index(self.MAGIC):
                    input(Text.MES_MAGIC.format(player.name))
                    if player.mp > 0:
                        player.mp -= 1
                        damage = 100 + player.level * 10
                        monster.hp -= damage
                        input(Text.MES_DAMAGE.format(damage))
                    else:
                        input(Text.MES_MP_IS_EMPTY)

                # アイテムの場合
                elif self.select_index == self.ACTION_LIST.index(self.ITEM):
                    used_item_flg = self.show_item_list(player, monster)
                    if not used_item_flg:
                        continue

                # にげるの場合
                elif self.select_index == self.ACTION_LIST.index(self.ESCAPE):
                    escape = randint(1, 100)
                    if escape >= 30:
                        input(Text.MES_ESCAPE)
                        break
                    else:
                        input(Text.MES_CAN_NOT_ESCAPE)

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

    def show_item_list(self, player, monster):
        """アイテム一覧を表示
        アイテムを使用した場合、Trueを返却
        """
        select_index = 0

        while True:
            Event.clear()
            print(Text.MES_HOW_TO_PLAY)
            print(Text.PLAYER_STATUS.format(
                player.name, player.hp, player.max_hp, player.mp, player.max_mp
            ))
            print(Text.MONSTER_STATUS.format(monster.name, monster.hp))
            print(Text.ITEM_LIST_PREFIX)

            # アイテムがある場合
            if player.item_list:
                for index, item in enumerate(player.item_list):

                    # 選択中のアイテムの場合
                    if index == select_index:
                        print(Text.ICON_SELECTED + item.title)
                    else:
                        print(Text.ICON_NOT_SELECTED + item.title)

            # アイテムがない場合
            else:
                print(Text.ITEM_LIST_NOTING)
                print(Text.ITEM_LIST_SUFFIX)
                Event.input()
                return
            print(Text.ITEM_LIST_SUFFIX)

            # キー入力待ち
            input_key = Process.input_player_key()

            # ITEMの場合、ESCの場合、
            if input_key == Process.ITEM or \
                    input_key == Process.ESC:
                break

            # UPの場合
            elif input_key == Process.UP:
                select_index = select_index - 1 \
                    if select_index > 0 else len(player.item_list) - 1

            # DOWNの場合
            elif input_key == Process.DOWN:
                select_index = select_index + 1 \
                    if select_index < len(player.item_list) - 1 else 0

            # DECISIONの場合、未入力の場合
            elif input_key == Process.DECISION or \
                    input_key == Process.EMPTY:
                item_object = player.item_list[select_index]
                print(Text.USE_ITEM_CONFIRM.format(item_object.description))
                answer = Event.input()

                # Yesの場合
                if Event.is_yes(answer):
                    if item_object == MapItem.HERBS:
                        player.hp += 100
                        if player.hp > player.max_hp:
                            player.hp = player.max_hp
                        player.item_list.pop(select_index)
                        select_index = 0
                        print(Text.MES_USE_HERB)
                        Event.input()
                        return True
                    else:
                        print(Text.MES_USE_EQUIPMENT)
                        Event.input()

            else:
                break
