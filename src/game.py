from src.controllers.inputKeyServer import InputKeyServer
from src.item import Item
from src.models.player import Player
from src.models.monster import Monster
from src.utils.const import (
    FieldAction,
    Mode,
)
from src.utils.event import Event
from src.views.buttle import Buttle
from src.views.map import Map
from src.views.text import Text


class Game:
    """ゲーム全体の流れを管理するクラス
    """

    def __init__(self):
        self.player = None
        self.map = None
        self.buttle = None
        self.game_flg = None
        self.mode_key = None

    def mode_start(self):
        """スタートモード
        """

        # タイトルの表示
        Event.output_title()

        # プレイヤー作成
        self.player = Player(Event.input_player_name())

        # マップの作成
        self.map = Map(Event.select_game_level())

        # プロローグ
        Event.output_opening_message(self.player.name)

        # フィールドモードへ
        self.mode_key = Mode.FIELD

    def mode_field(self):
        """モードフィールド
        """

        # マップ表示
        self.map.output()

        key_obj = InputKeyServer.get_input_key_obj(Event.input_character())

        # モード変更用
        next_mode_key = None

        # プレイヤーが動く場合
        if key_obj.field_action == FieldAction.MOVE:
            height, width = key_obj.move_map()

            field_item = self.map.get_next_field_item(height, width)

            # プリエヤーが移動できる場合
            if self.map.can_move_player(field_item):
                self.map.change_field(height, width)

            else:
                print(Text.MES_CAN_NOT_MOVE)
                Event.input()

            # ゴール
            if field_item == Item.GOAL.value:
                next_mode_key = Mode.GAME_CLEAR

            # プレイヤーがアイテム取得できる場合
            if self.map.is_item(field_item):
                self.player.append_item(field_item)

            # エンカウント判定
            if self.buttle.is_encount_monster():
                next_mode_key = Mode.BUTTLE


        # 他の画面に切り替える場合
        if key_obj.field_action == FieldAction.CHANGE:
            next_mode_key = key_obj.change_display()

        # モードを変更する場合
        if next_mode_key:
            self.mode_key = next_mode_key

    def mode_item_list(self):
        """アイテム一覧モード
        """
        self.player.open_item_list()
        self.mode_key = Mode.FIELD

    def mode_buttle(self):
        """バトルモード
        """

        # モンスター作成
        monster = Monster(self.buttle.counter)

        # バトル
        self.mode_key = self.buttle.start(self.player, monster)

    def mode_status(self):
        """プレイヤーのステータス詳細を表示
        """
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)

        # ステータスを表示
        self.player.output_status()
        self.player.output_status_detail()
        Event.input()

        # フィールドモードへ
        self.mode_key = Mode.FIELD

    def mode_help(self):
        """ヘルプモード
        """

        # ヘルプ表示
        Event.clear()
        print('show help')
        Event.input()

        # フィールドモードへ
        self.mode_key = Mode.FIELD

    def mode_game_escape(self):
        """エスケープモード
        """

        Event.clear()
        print(Text.STRING_DECORATION)

        # 終了
        if Event.confirm():
            Event.clear()
            print(Text.GAME_ESCAPE)
            self.game_flg = False

        # 戻る
        else:
            self.mode_key = Mode.FIELD

    def mode_game_over(self):
        """ゲームオーバーモード
        """

        # ゲームオーバー
        Event.clear()
        print(Text.GAME_OVER)

        self.game_flg = False

    def mode_game_clear(self):
        """ゲームクリアモード
        """

        # ゲームクリア
        Event.clear()
        print(Text.GAME_CLEAR)

        self.game_flg = False

    def start(self):
        """メインループ
        """
        self.buttle = Buttle()
        self.game_flg = True
        self.mode_key = Mode.START

        # モード定義
        mode_def = {
            Mode.START: self.mode_start,
            Mode.FIELD: self.mode_field,
            Mode.ITEM_LIST: self.mode_item_list,
            Mode.STATUS: self.mode_status,
            Mode.HELP: self.mode_help,
            Mode.BUTTLE: self.mode_buttle,
            Mode.ESCAPE: self.mode_game_escape,
            Mode.GAME_CLEAR: self.mode_game_clear,
            Mode.GAME_OVER: self.mode_game_over,
        }

        while self.game_flg:

            # モード取得
            mode = mode_def[self.mode_key]

            # モード実行
            mode()
