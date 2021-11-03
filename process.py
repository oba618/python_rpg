from buttle import Buttle
from event import Event
from item import Item
from key import Key
from map import Map
from monster import Monster
from player import Player
from text import Text


class Process:
    """ゲーム全体の流れを記述するクラス
    """

    def __init__(self):
        self._player = None
        self._map = None
        self._escape_flg = False
        self._buttle_flg = False
        self._counter = 0
        self.start()

    def start(self):
        """ゲームススタート：概要を一覧で記述
        """

        # タイトルの表示
        Event.show_title()

        # プレイヤー作成
        self._player = Player(Event.input_player_name())

        # マップの作成
        self._map = Map(Event.select_game_level())

        # プロローグ
        Event.show_prologue(self._player.name)

        # メインループ判定
        while self.check_main_loop():

            # マップ表示
            self._map.show()

            # キーに応じたアクション
            self.action_player_key(Event.check_player_key())

            # エンカウント判定
            self.check_start_buttle()

        # エピローグ（終わり）
        self.show_epilogue()

    def check_main_loop(self) -> bool:
        """メインループを続けるか判定

        Returns:
            bool: ループを続けるか否か
        """
        if self._player.hp <= 0:
            return False

        if self._escape_flg:
            return False

        if self._map.field == Item.GOAL.value:
            return False

        if self._map.goal_flg is True:
            return False

        return True

    def show_epilogue(self):
        """エピローグを表示する
        """
        # 移動先が、ゴールの場合
        if self._map.field == Item.GOAL.value:
            Event.clear()
            print(Text.GAME_CLEAR)
            return

        # プレイヤーのHPが0以下になった場合
        if self._player.hp < 0:
            Event.clear()
            print(Text.GAME_OVER)
            return

        # ESCキーでゲーム終了の場合
        if self._escape_flg:
            Event.clear()
            print(Text.GAME_OVER)
            return

        if self._map.goal_flg is True:
            Event.clear()
            print(Text.GAME_CLEAR)
            return

    def show_player_status(self):
        """プレイヤーのステータス詳細を表示

        Args:
            player (Player): インスタンス
        """
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # 次レベルまでの必要経験値
        self.required_exp = self._player.level**2 - self._player.exp

        # 概要ステータスを表示
        print(Text.PLAYER_STATUS.format(
            self._player.name,
            self._player.hp,
            self._player.max_hp,
            self._player.mp,
            self._player.max_mp,
        ))

        # 詳細ステータスを表示
        print(Text.PLAYER_STATUS_DETAIL.format(
            self._player.level,
            self._player.exp,
            self.required_exp,
            self._player.power,
            self._player.defense,
        ))
        Event.input()

    def show_item_list(self):
        """アイテム一覧を表示するループ
        """
        select_index = 0

        while True:
            Event.clear()
            print(Text.MES_HOW_TO_PLAY)
            print(Text.PLAYER_STATUS.format(
                self._player.name, self._player.hp, self._player.max_hp, self._player.mp, self._player.max_mp
            ))
            print(Text.ITEM_LIST_PREFIX)

            # アイテムがある場合
            if self._player.item_list:
                for index, item in enumerate(self._player.item_list):

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
            input_key = Event.input_player_key()

            # ITEMの場合、ESCの場合、
            if input_key == Key.ITEM or \
                    input_key == Key.ESC:
                break

            # UPの場合
            elif input_key == Key.UP:
                select_index = select_index - 1 \
                    if select_index > 0 else len(self._player.item_list) - 1

            # DOWNの場合
            elif input_key == Key.DOWN:
                select_index = select_index + 1 \
                    if select_index < len(self._player.item_list) - 1 else 0

            # DECISIONの場合、未入力の場合
            elif input_key == Key.DECISION or \
                    input_key == Key.EMPTY:
                item_object = self._player.item_list[select_index]
                print(Text.USE_ITEM_CONFIRM.format(item_object.description))
                answer = Event.input()

                # Yesの場合
                if Event.is_yes(answer):
                    if item_object == Item.HERBS:
                        self._player.hp += 100
                        if self._player.hp > self._player.max_hp:
                            self._player.hp = self._player.max_hp
                        self._player.item_list.pop(select_index)
                        select_index = 0
                        print(Text.MES_USE_HERB)
                        Event.input()
                    else:
                        print(Text.MES_USE_EQUIPMENT)
                        Event.input()

            else:
                break

    @classmethod
    def create_height_and_width(self, player_key):
        height = 0
        width = 0

        # 下へ
        if player_key == Key.DOWN:
            height = 1

        # 左へ
        elif player_key == Key.LEFT:
            width = -1

        # 右へ
        elif player_key == Key.RIGHT:
            width = 1

        # 上へ
        elif player_key == Key.UP:
            height = -1

        return (height, width, )

    def move_map(self, player_key: str):

        height, width = self.create_height_and_width(player_key)

        # マップを移動
        item = self._map.move(height, width)

        # アイテム取得
        if item:
            self._player.get_item(item)

        # エンカウント用
        self._counter += 1

        self._buttle_flg = Event.is_encount(self._counter)

    def start_buttle(self):
        """バトル開始準備
        """

        # モンスター作成
        monster = Monster(self._counter)

        # バトルクラスへ
        buttle = Buttle(self._player, monster)

        # バトル
        buttle.start_buttle()

        # バトル終了
        self._buttle_flg = False

    def action_player_key(self, player_key):

        # ESCキーを押した場合
        if player_key == Key.ESC:
            self._escape_flg = Event.confirmation()

        # ITEMキーを押した場合
        elif player_key == Key.ITEM:
            pass

            # アイテム画面へ
            self.show_item_list()

        # HELPキーを押した場合
        elif player_key == Key.HELP:
            pass

        # STATUS木ーを押した場合
        elif player_key == Key.STATUS:

            # ステータス画面へ
            self.show_player_status()

        # DECISIONキーを押した場合
        elif player_key == Key.DECISION:
            pass

        # 移動キーを押した場合
        elif player_key in Key.MOVE_KEY_LIST:
            self.move_map(player_key)

        else:
            return

    def check_start_buttle(self):
        """バトル開始判定
        """

        if self._buttle_flg:

            # バトル画面へ
            self.start_buttle()
