from random import random
import sys

from src.controllers.inputKey import InputKey
from src.controllers.inputKeyServer import InputKeyServer
from src.models.monster import Monster
from src.models.player import Player
from src.utils.const import (
    ButtleAction,
    ItemListAction,
    Mode,
)
from src.utils.event import Event
from src.views.text import Text


class Buttle:
    """バトル画面に遷移するイメージのクラス
    """

    def __init__(self):
        self.player = None
        self.monster = None
        self.appear_flg = None
        self.monster_action_flg = None
        self.mode = None
        self.buttle_flg = None
        self.counter = 0

    def mode_buttle(self):
        """バトルモード
        """
        self.player.select_index = 0

        while self.mode == Mode.BUTTLE:

            # 画面表示
            self.output()

            # アクションリスト表示
            self.player.output_action_list()

            # キー入力に対応したアクション
            self.action_in_buttle(
                InputKeyServer.get_input_key_obj(Event.input_character()))

            # モンスター死亡判定
            if self.is_dead(self.monster):

                # プレイヤー勝利
                self.player.win_buttle(self.monster)

                # フィールドモードへ
                self.mode = Mode.FIELD
                self.buttle_flg = False
                return

            # モンスターの攻撃
            if self.monster.action_flg:
                self.monster.attack(self.player)

            # プレイヤー死亡判定
            if self.is_dead(self.player):

                # ゲームオーバーモードへ
                self.mode = Mode.GAME_OVER
                self.buttle_flg = False
                return

    def action_in_buttle(self, key_obj: InputKey):
        """バトルモードでのアクション

        Args:
            key_obj (InputKey): キーオブジェクト
        """

        # カーソル動く
        if key_obj.buttle_action == ButtleAction.MOVE:
            self.player.select_index = key_obj.move_cursor(
                len(self.player.action_list),
                self.player.select_index,
            )

        # 決定
        if key_obj.buttle_action == ButtleAction.DECISION:
            self.mode = self.player.action_in_buttle(
                self.monster,
            )

        # 画面遷移
        if key_obj.buttle_action == ButtleAction.CHANGE:
            self.mode = key_obj.change_display()

    def is_dead(self, target) -> bool:
        """死亡判定

        Args:
            target (Player or Monster): ターゲット

        Returns:
            bool: 死亡判定
        """
        return target.hp <= 0

    def output(self):
        """ディスプレイ表示
        """

        # 上部表示
        Event.clear()
        self.output_top()

        # モンスター登場
        if self.monster.appear_flg:
            self.monster.appear()
            self.monster.appear_flg = False

    def output_top(self):
        """ディスプレイ上部表示
        """

        # 遊び方
        print(Text.MES_HOW_TO_PLAY)

        # プレイヤーステータス
        print(Text.PLAYER_STATUS.format(
            self.player.name,
            self.player.hp,
            self.player.max_hp,
            self.player.mp,
            self.player.max_mp
        ))

        # モンスターステータス
        print(Text.MONSTER_STATUS.format(
            self.monster.name,
            self.monster.hp,
        ))

    def show_items(self, item_list: list):
        """アイテム表示

        Args:
            item_list (list): アイテム一覧
        """

        print(Text.ITEM_LIST_PREFIX)

        # アイテムがある場合
        if item_list:
            for index, item in enumerate(item_list):

                # 選択中のアイテムの場合は'[※]'を表示する
                if index == self.player.select_index:
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

    def is_encount_monster(self) -> bool:
        """モンスターと戦闘するか否か

        Returns:
            bool: モンスターと戦闘するか否か
        """
        self.counter += 1

        return int(random() * 100) % 20 == 0 or self.counter % 50 == 0

    def mode_item_list(self):
        """アイテム一覧モード
        """
        self.player.open_item_list()
        self.mode = Mode.BUTTLE

    def mode_status(self):
        """プレイヤーのステータス詳細を表示
        """

        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # 概要ステータスを表示
        self.player.output_status()
        self.player.output_status_detail()
        Event.input()

        # バトルに戻る
        self.mode = Mode.BUTTLE

    def mode_help(self):
        """ヘルプモード
        """

        # ヘルプ表示
        Event.clear()
        print('show help')
        Event.input()

        self.mode = Mode.BUTTLE

    def mode_game_escape(self):
        """エスケープモード
        """

        self.output()
        print(Text.STRING_DECORATION)

        # 確認
        if Event.confirm():

            # ゲーム終了
            Event.clear()
            print(Text.GAME_ESCAPE)
            sys.exit()

        else:
            self.mode = Mode.BUTTLE

    def mode_field(self):
        """フィールドモードへ
        """
        self.buttle_flg = False

    def start(self, player: Player, monster: Monster) -> Mode:
        """バトルスタート

        Args:
            player (Player): プレイヤー
            monster (Monster): モンスター

        Returns:
            Mode: モード
        """
        self.buttle_flg = True
        self.mode = Mode.BUTTLE
        self.appear_flg = True
        self.monster_action_flg = False

        self.player = player
        self.monster = monster

        # モード定義
        mode_def = {
            Mode.FIELD: self.mode_field,
            Mode.BUTTLE: self.mode_buttle,
            Mode.ITEM_LIST: self.mode_item_list,
            Mode.ESCAPE: self.mode_game_escape,
            Mode.STATUS: self.mode_status,
            Mode.HELP: self.mode_help,
        }

        while self.buttle_flg:

            # モード選択
            mode = mode_def.get(self.mode)

            # モード実行
            mode()

        return self.mode
