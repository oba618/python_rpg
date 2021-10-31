from buttle import Buttle
from event import Event
from map import Map, MapItem
from monster import Monster
from player import Player
from process import Process
from text import Text


def main():

    # ゲームプロセス初期化
    process = Process()

    # タイトルの表示
    process.show_title()

    # プレイヤー作成
    player = Player(process.input_player_name())

    # マップの作成
    map = Map(process.select_game_level())

    # テキストを表示
    process.show_epilogue(player.name)

    # メインループ
    while True:
        map.field = ''
        map.show()
        player_key = process.input_player_key()
        if not player_key:
            continue

        # ESCキーを押した場合
        if player_key == process.ESC:
            if Event.confirmation():
                Event.clear()
                print(Text.GAME_OVER)
                break
            else:
                continue

        # ITEMキーを押した場合
        elif player_key == process.ITEM:
            show_item_list(player)
            continue

        # HELPキーを押した場合
        elif player_key == process.HELP:
            continue

        # STATUS木ーを押した場合
        elif player_key == process.STATUS:
            Event.clear()
            print(Text.MES_HOW_TO_PLAY)
            process.show_player_status(player)
            continue

        # DECISIONキーを押した場合
        elif player_key == process.DECISION:
            continue

        # 移動キーを押した場合
        elif player_key == process.UP or player_key == process.DOWN or\
                player_key == process.LEFT or player_key == process.RIGHT:
            map.move(player_key)

        # その他のキーを押した場合
        else:
            continue

        # 移動先が、壁の場合
        if map.field == MapItem.BLOCK.value:
            print(Text.MES_CAN_NOT_MOVE)
            Event.input()
            continue

        # 移動先が、ゴールの場合
        if map.field == MapItem.GOAL.value:
            Event.clear()
            print(Text.GAME_CLEAR)
            break

        # 移動先が、空地の場合
        if map.field == MapItem.EMPTY.value:
            map.field = ''

        # 移動先が、アイテムの場合
        if map.field:
            player.get_item(map.field)

        # エンカウント判定
        if Event.is_encount(map.counter):
            monster = Monster(map.counter)
            Buttle().buttle(player, monster)

        # プレイヤーのHPが0以下になった場合
        if player.hp < 0:
            Event.clear()
            print(Text.GAME_OVER)
            break


def show_item_list(player: Player):
    """アイテム一覧を表示するループ
    """
    select_index = 0

    while True:
        Event.clear()
        print(Text.MES_HOW_TO_PLAY)
        print(Text.PLAYER_STATUS.format(
            player.name, player.hp, player.max_hp, player.mp, player.max_mp
        ))
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
                else:
                    print(Text.MES_USE_EQUIPMENT)
                    Event.input()

        else:
            break


if __name__ == '__main__':
    main()
