from io import StringIO

from map import MapItem
from player import Player


class TestPlayer:
    def test_create_instance(self):
        """正常
        プレイヤーが作成されること
        """
        player_name = 'test_player'
        player = Player(player_name)

        assert player.name == player_name
        assert player.max_hp == player.DEFAULT_INITIAL_HP
        assert player.hp == player.DEFAULT_INITIAL_HP
        assert player.max_mp == player.DEFAULT_INITIAL_MP
        assert player.mp == player.DEFAULT_INITIAL_MP
        assert player.power == player.DEFAULT_INITIAL_POWER
        assert player.defense == player.DEFAULT_INITIAL_DEFENSE
        assert player.exp == player.DEFAULT_INITIAL_EXP
        assert player.level == player.DEFAULT_INITIAL_LEVEL
        assert player.item_list == player.DEFAULT_INITIAL_ITEM_LIST

    def test_create_instance_setter(self):
        """正常
        プレイヤーの値が更新されること
        """
        player_name = 'test_player'
        player = Player(player_name)

        expect_name = 'changed_name'
        expect_max_hp = 1000
        expect_hp = 2000
        expect_max_mp = 3000
        expect_mp = 4000
        expect_power = 5000
        expect_defense = 6000
        expect_exp = 7000
        expect_level = 8000
        expect_item_list = ['test_is_ok']

        # 更新
        player.name = expect_name
        player.max_hp = expect_max_hp
        player.hp = expect_hp
        player.max_mp = expect_max_mp
        player.mp = expect_mp
        player.power = expect_power
        player.defense = expect_defense
        player.exp = expect_exp
        player.level = expect_level
        player.item_list = expect_item_list

        assert player.name == expect_name
        assert player.max_hp == expect_max_hp
        assert player.hp == expect_hp
        assert player.max_mp == expect_max_mp
        assert player.mp == expect_mp
        assert player.power == expect_power
        assert player.defense == expect_defense
        assert player.exp == expect_exp
        assert player.level == expect_level
        assert player.item_list == expect_item_list

    def test_level_up(self):
        """正常
        数値が更新されること
        """
        player_name = 'test_player'
        player = Player(player_name)

        assert player.level == 1

        player.level_up()

        assert player.max_hp \
            == player.DEFAULT_INITIAL_HP + player.ADD_MAX_HP
        assert player.power \
            == player.DEFAULT_INITIAL_POWER + player.ADD_POWER
        assert player.defense \
            == player.DEFAULT_INITIAL_DEFENSE + player.ADD_DEFENCE
        assert player.level \
            == player.DEFAULT_INITIAL_LEVEL + player.ADD_LEVEL

    def test_level_up_100(self):
        """正常
        レベルが100になること
        """
        player_name = 'test_player'
        player = Player(player_name)

        for i in range(99):
            player.level_up()

        assert player.level == 100

    def test_get_item(self, monkeypatch):
        """正常
        アイテムリストにアイテムが入ること
        """
        monkeypatch.setattr('sys.stdin', StringIO(''))

        player_name = 'test_player'
        player = Player(player_name)

        assert player.item_list == []

        player.get_item(MapItem.WEAPON.value)
        player.get_item(MapItem.SIELD.value)
        player.get_item(MapItem.HERBS.value)

        assert MapItem(MapItem.WEAPON.value) in player.item_list
        assert MapItem(MapItem.SIELD.value) in player.item_list
        assert MapItem(MapItem.HERBS.value) in player.item_list
