from io import StringIO

from process import Process
from text import Text


class TestMain:
    def test_show_title(self, monkeypatch, capfd):
        monkeypatch.setattr('sys.stdin', StringIO(''))
        Process.show_title()
        out, err = capfd.readouterr()

        assert out == Text.TITLE + '\n'
        assert err == ''

    def test_input_player_name(self, monkeypatch):
        expect_player_name = 'テストプレイヤー'
        monkeypatch.setattr('sys.stdin', StringIO(expect_player_name))

        assert Process.input_player_name() == expect_player_name

    def test_confirm_input_player_name(self, monkeypatch):
        expect_player_name = 'テストプレイヤー'
        monkeypatch.setattr('sys.stdin', StringIO('y'))
        player_name = Process.confirm_input_player_name(expect_player_name)

        assert player_name == expect_player_name
