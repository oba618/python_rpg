from io import StringIO

from models.player import Player
from src.game import Game
from views.text import Text


class TestProcess:
    def test_show_title(self, monkeypatch, capfd):
        """正常
        タイトrが表示されること
        """
        monkeypatch.setattr('sys.stdin', StringIO(''))
        Game.show_title()
        out, err = capfd.readouterr()

        assert out == Text.TITLE + '\n'
        assert err == ''

    def test_input_player_name(self, monkeypatch):
        """正常
        プレイヤー名が入力できること
        """
        expect_player_name = 'テストプレイヤー'
        monkeypatch.setattr('sys.stdin', StringIO(expect_player_name))

        assert Game.input_player_name() == expect_player_name

    def test_input_player_name_long_name(self, monkeypatch):
        """正常
        プレイヤー名が10文字以上の場合、空文字列が返却されること
        """
        expect_player_name = ''
        bad_input = 'とてもながいプレイヤーのなまえ'
        monkeypatch.setattr('sys.stdin', StringIO(bad_input))

        assert Game.input_player_name() == expect_player_name

    def test_input_player_name_notingh(self, monkeypatch):
        """正常
        プレイヤー名が未入力の場合、空文字列が返却されること
        """
        expect_player_name = ''
        bad_input = None
        monkeypatch.setattr('sys.stdin', StringIO(bad_input))

        assert Game.input_player_name() == expect_player_name

    def test_confirm_input_player_name_answer_is_yes(self, monkeypatch):
        """正常
        返答がYESの場合、プレイヤー名が返却されること
        """
        expect_player_name = 'テストプレイヤー'
        monkeypatch.setattr('sys.stdin', StringIO('y'))
        player_name = Game.confirm_input_player_name(expect_player_name)

        assert player_name == expect_player_name

    def test_confirm_input_player_name_answer_is_no(self, monkeypatch):
        """正常
        返答がNoの場合、空文字列が返却されること
        """
        player_name = 'テストプレイヤー'
        expect_player_name = ''
        monkeypatch.setattr('sys.stdin', StringIO('n'))
        player_name = Game.confirm_input_player_name(player_name)

        assert player_name == expect_player_name

    def test_input_player_key(self, monkeypatch):
        """正常
        予測されるキーが入力された場合、文字列が返却されること
        """
        # Qの場合
        expect_string = 'q'
        input_key_list = ['q', 'Q', 'ｑ', 'Ｑ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Wの場合
        expect_string = 'w'
        input_key_list = ['w', 'W', 'ｗ', 'Ｗ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Eの場合
        expect_string = 'e'
        input_key_list = ['e', 'E', 'え', 'Ｅ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Aの場合
        expect_string = 'a'
        input_key_list = ['a', 'A', 'あ', 'Ａ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Sの場合
        expect_string = 's'
        input_key_list = ['s', 'S', 'ｓ', 'Ｓ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Dの場合
        expect_string = 'd'
        input_key_list = ['d', 'D', 'ｄ', 'Ｄ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Zの場合
        expect_string = 'z'
        input_key_list = ['z', 'Z', 'ｚ', 'Ｚ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Xの場合
        expect_string = 'x'
        input_key_list = ['x', 'X', 'ｘ', 'Ｘ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # Cの場合
        expect_string = 'c'
        input_key_list = ['c', 'C', 'ｃ', 'Ｃ']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

        # 空文字の場合
        expect_string = ''
        input_key_list = ['', ' ', '　']
        for input_key in input_key_list:
            monkeypatch.setattr('sys.stdin', StringIO(input_key))
            assert Game.input_player_key() == expect_string

    def test_input_player_key_out_of_range(self, monkeypatch, capfd):
        """正常
        予測外のキーが入力された場合、エラーメッセージが標準出力されること
        """
        # test_1
        input_key = 't'
        monkeypatch.setattr('sys.stdin', StringIO(input_key))
        Game.input_player_key()
        out, err = capfd.readouterr()

        assert out == Text.MES_CAN_NOT_USE_KEY + '\n'
        assert err == ''

        # test_2
        input_key = 'テスト'
        monkeypatch.setattr('sys.stdin', StringIO(input_key))
        Game.input_player_key()
        out, err = capfd.readouterr()

        assert out == Text.MES_CAN_NOT_USE_KEY + '\n'
        assert err == ''

        # test_3
        input_key = '◎'
        monkeypatch.setattr('sys.stdin', StringIO(input_key))
        Game.input_player_key()
        out, err = capfd.readouterr()

        assert out == Text.MES_CAN_NOT_USE_KEY + '\n'
        assert err == ''

    def test_show_player_status(self, capfd, monkeypatch):
        """正常
        プレイヤーに応じたステータスが表示されること
        """
        player_name = 'test_player'
        player = Player(player_name)
        required_exp = player.level**2 - player.exp
        expect_string = \
            Text.PLAYER_STATUS.format(
                player.name,
                player.hp,
                player.max_hp,
                player.mp,
                player.max_mp,
            ) \
            + '\n' \
            + Text.PLAYER_STATUS_DETAIL.format(
                player.level,
                player.exp,
                required_exp,
                player.power,
                player.defense,
            ) \
            + '\n'

        monkeypatch.setattr('sys.stdin', StringIO(''))
        Game.show_player_status(player)
        out, err = capfd.readouterr()

        assert out == expect_string
        assert err == ''
