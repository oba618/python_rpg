from event import Event
from text import Text


class Process:
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'
    ESC = 'q'
    ITEM = 'e'
    STATUS = 'z'
    DECISION = 'x'
    HELP = 'c'
    EMPTY = ''
    KEY_LIST = {
        UP: ['w', 'W', 'ｗ', 'Ｗ'],
        DOWN: ['s', 'S', 'ｓ', 'Ｓ'],
        LEFT: ['a', 'A', 'あ', 'Ａ'],
        RIGHT: ['d', 'D', 'ｄ', 'Ｄ'],
        ESC: ['q', 'Q', 'ｑ', 'Ｑ'],
        ITEM: ['e', 'E', 'え', 'Ｅ'],
        STATUS: ['z', 'Z', 'ｚ', 'Ｚ'],
        DECISION: ['x', 'X', 'ｘ', 'Ｘ'],
        HELP: ['c', 'C', 'ｃ', 'Ｃ'],
        EMPTY: ['', ' ', '　'],
    }

    @staticmethod
    def show_title():
        """タイトルを表示
        """
        Event.clear()
        print(Text.TITLE)
        Event.input()

    @staticmethod
    def show_epilogue(player_name):
        """エピローグを表示

        Args:
            player_name (str): プレイヤー名
        """
        Event.clear()
        print(Text.MES_GAME_MISSION.format(player_name))
        Event.input()

    @classmethod
    def input_player_name(cls) -> str:
        """プレイヤーの名前を入力

        Returns:
            str: プレイヤー名
        """
        player_name = ''
        while not player_name:

            Event.clear()
            print(Text.MES_INPUT_PLAYER_NAME)
            player_name = Event.input()

            # プレイヤー名が長い場合
            if len(player_name) >= Text.PLAYER_NAME_MAX_LENGTH:
                print(Text.MES_PLAYER_NAME_IS_TOO_LONG)
                Event.input()
                player_name = ''
                continue

            # プレイヤー名が未入力の場合
            if len(player_name) == 0:
                continue

            # 決定の確認
            player_name = cls.confirm_input(player_name)

        return player_name

    @classmethod
    def select_game_level(cls) -> str:
        """ゲームレベル選択

        Returns:
            str: ゲームレベル
        """
        game_level = ''
        while not game_level:
            Event.clear()
            print(Text.MES_SELECT_GAME_LEVEL)
            game_level = Event.input()

            if game_level in ['1', '2', '3']:
                game_level = cls.confirm_input(game_level)

            else:
                game_level = ''

        return game_level

    @staticmethod
    def confirm_input(item: str) -> str:
        """応答がYesかNoを確認

        Args:
            item (str): 文字列

        Returns:
            str: 文字列
        """
        print(Text.QUESTION_ANSWER.format(item))
        answer = Event.input()
        if Event.is_yes(answer):
            return item
        else:
            return ''

    @classmethod
    def input_player_key(cls) -> str:
        """標準入力の受付

        Returns:
            str: バリデーションされた文字列
        """
        while True:
            input_key = Event.input()
            for key, value in cls.KEY_LIST.items():
                if input_key in value:
                    return key

            # 不正な入力の場合
            else:
                print(Text.MES_CAN_NOT_USE_KEY)

    @staticmethod
    def show_player_status(player):
        """プレイヤーのステータス詳細を表示

        Args:
            player (Player): インスタンス
        """
        # 次レベルまでの必要経験値
        required_exp = player.level**2 - player.exp

        # 概要ステータスを表示
        print(Text.PLAYER_STATUS.format(
            player.name,
            player.hp,
            player.max_hp,
            player.mp,
            player.max_mp,
        ))

        # 詳細ステータスを表示
        print(Text.PLAYER_STATUS_DETAIL.format(
            player.level,
            player.exp,
            required_exp,
            player.power,
            player.defense,
        ))
        Event.input()
