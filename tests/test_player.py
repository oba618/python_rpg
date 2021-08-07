from player import Player


class TestPlayer:
    def test_create_instance(self):
        player_name = 'test_player'
        player = Player(player_name)

        assert player.name == player_name
