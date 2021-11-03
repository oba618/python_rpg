from event import Event
from item import Item
from key import Key
from random import randint
from text import Text


class Buttle:
    """バトル画面に遷移するイメージのクラス

    Args:
        player (Player): プレイヤー
        monster (Monster): モンスター
    """

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

    def __init__(self, player, monster):
        self._player = player
        self._monster = monster
        self._appear_flg = True
        self._end_flg = False
        self._monster_action_flg = False
        self._select_index = 0

    def start_buttle(self):

        while self.check_buttle_loop():

            # 画面表示
            self.show_display()
            if self._appear_flg:
                self._appear_flg = False
                continue

            # HPを確認
            self.check_monster_hp()
            self.check_player_hp()
            if self._end_flg:
                return

            # アクションリスト表示
            self.show_action_list()

            # キー入力受付
            input_key = Event.input_player_key()

            # キー入力に応じてアクション
            self.action_player_key(input_key)

            # 攻撃によってモンスターのHPが0以下になった場合
            if self._monster.hp <= 0:
                continue

            # モンスターの攻撃
            if self._monster_action_flg:
                self.action_monster()

    def show_item_list(self):
        """アイテム一覧を表示
        """
        self._select_index = 0
        loop_flg = True

        while loop_flg:
            Event.clear()

            # アイテム一覧を表示
            self.show_display_top()
            self.show_items()

            # アイテムが無ければリターン
            if not self._player.item_list:
                loop_flg = False
                continue

            # キー入力待ち
            input_key = Event.input_player_key()

            # アイテム一覧内でのセレクト
            loop_flg = self.select_use_item(input_key)

        self._select_index = 0

    def show_display(self):

        Event.clear()
        self.show_display_top()

        # モンスター登場
        if self._appear_flg:
            print(Text.MES_APPEAR_MONSTER.format(self._monster.name))
            Event.input()

    def show_display_top(self):

        print(Text.MES_HOW_TO_PLAY)
        print(Text.PLAYER_STATUS.format(
            self._player.name,
            self._player.hp,
            self._player.max_hp,
            self._player.mp,
            self._player.max_mp
        ))

        print(Text.MONSTER_STATUS.format(
            self._monster.name,
            self._monster.hp,
        ))

    def show_items(self):

        print(Text.ITEM_LIST_PREFIX)

        # アイテムがある場合
        if self._player.item_list:
            for index, item in enumerate(self._player.item_list):

                # 選択中のアイテムの場合は'[※]'を表示する
                if index == self._select_index:
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

    def check_monster_hp(self):
        if self._monster.hp <= 0:
            print(Text.KNOCK_OUT_MONSTER.format(self._monster.name))
            Event.input()

            # 経験値獲得
            self._player.exp += self._monster.level
            print(Text.MES_GET_EXP.format(self._monster.level))
            Event.input()

            # レベルの二乗より経験値が大きい場合、レベルアップ
            if self._player.level**2 <= self._player.exp:
                self._player.level_up()
                print(Text.MES_LEVEL_UP.format(self._player.name, self._player.level))
                Event.input()

            self._end_flg = True

    def check_player_hp(self):
        if self._player.hp <= 0:
            print(Text.KNOCK_OUT_PLAYER.format(self._player.name))
            Event.input()

            self._end_flg = True

    def show_action_list(self):
        print(Text.MES_CHOOSE_ACTION)
        for index, action in enumerate(self.ACTION_LIST):
            if self._select_index == index:
                print(Text.ICON_SELECTED + action)
            else:
                print(Text.ICON_NOT_SELECTED + action)

    def action_player_key(self, input_key):

        # UPの場合
        if input_key == Key.UP:
            self._select_index = self._select_index - 1 \
                if self._select_index > 0 \
                else len(self.ACTION_LIST) - 1

        # DOWNの場合
        elif input_key == Key.DOWN:
            self._select_index = self._select_index + 1 \
                if self._select_index < len(self.ACTION_LIST) - 1 \
                else 0

        # ESCの場合
        elif input_key == Key.ESC:
            pass

        # STATUSの場合
        elif input_key == Key.STATUS:
            pass

        # HELPの場合
        elif input_key == Key.HELP:
            pass

        # ITEMの場合
        elif input_key == Key.ITEM:
            self.show_item_list()

        # DECESIONの場合、未入力の場合
        elif input_key == Key.DECISION or \
                input_key == Key.EMPTY:

            # プレイヤーの行動
            self.action_player()

        # 無効なキーの場合
        else:
            input(Text.MES_CAN_NOT_USE_KEY)

    def check_buttle_loop(self):
        return not self._end_flg

    def action_monster(self):

        input(Text.MES_ATTACK_FROM_MONSTER.format(self._monster.name))
        damage = self._monster.power + randint(0, self._monster.level) - self._player.defense
        if damage < 0:
            damage = 0
        self._player.hp -= damage
        input(Text.MES_DAMAGE.format(damage))

        self._monster_action_flg = False

    def select_use_item(self, input_key: str) -> bool:
        """戦闘中アイテム一覧、セレクト

        Args:
            input_key (str): インプットキー

        Returns:
            bool: アイテム一覧を開いたままにするか否か
        """

        # ITEMの場合、ESCの場合、
        if input_key == Key.ITEM or \
                input_key == Key.ESC:

            return False

        # UPの場合
        elif input_key == Key.UP:
            self._select_index = self._select_index - 1 \
                if self._select_index > 0 \
                else len(self._player.item_list) - 1

            return True

        # DOWNの場合
        elif input_key == Key.DOWN:
            self._select_index = self._select_index + 1 \
                if self._select_index < len(self._player.item_list) - 1 \
                else 0

            return True

        # DECISIONの場合、未入力の場合
        elif input_key == Key.DECISION or \
                input_key == Key.EMPTY:
            item_object = self._player.item_list[self._select_index]
            print(Text.USE_ITEM_CONFIRM.format(item_object.description))
            answer = Event.input()

            # Yesの場合
            if Event.is_yes(answer):
                if item_object == Item.HERBS:
                    self._player.hp += 100
                    if self._player.hp > self._player.max_hp:
                        self._player.hp = self._player.max_hp
                    self._player.item_list.pop(self._select_index)
                    print(Text.MES_USE_HERB)
                    Event.input()
                    self._monster_action_flg = True

                    return

                else:
                    print(Text.MES_USE_EQUIPMENT)
                    Event.input()

        # 想定外のキーの場合はアイテム一覧から抜ける
        else:
            return

    def action_player(self):
        """プレイヤーのアクション
        """

        # こうげきの場合
        if self._select_index == self.ACTION_LIST.index(self.ATTACK):
            # プレイヤーの攻撃
            input(Text.MES_ATTACK_FROM_PLAYER.format(self._player.name))
            damage = self._player.power + randint(0, self._player.level)
            input(Text.MES_DAMAGE.format(damage))
            self._monster.hp -= damage
            self._monster_action_flg = True

        # まほうの場合
        elif self._select_index == self.ACTION_LIST.index(self.MAGIC):
            input(Text.MES_MAGIC.format(self._player.name))
            if self._player.mp > 0:
                self._player.mp -= 1
                damage = 100 + self._player.level * 10
                self._monster.hp -= damage
                input(Text.MES_DAMAGE.format(damage))
                self._monster_action_flg = True
            else:
                input(Text.MES_MP_IS_EMPTY)

        # アイテムの場合
        elif self._select_index == self.ACTION_LIST.index(self.ITEM):
            self.show_item_list()

        # にげるの場合
        elif self._select_index == self.ACTION_LIST.index(self.ESCAPE):
            escape = randint(1, 100)
            if escape >= 30:
                input(Text.MES_ESCAPE)
                self._end_flg = True
            else:
                input(Text.MES_CAN_NOT_ESCAPE)
                self._monster_action_flg = True
