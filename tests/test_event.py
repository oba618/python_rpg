from event import Event


class TestEvent:
    def test_clear(self, capfd):
        """正常
        標準出力が改ページコードのみ表示されること
        """
        test_string = 'test_string'
        print(test_string)
        out, err = capfd.readouterr()

        assert out == test_string + '\n'
        assert err == ''

        Event.clear()
        out, err = capfd.readouterr()

        assert out == '\x0c'
        assert err == ''

    def test_is_yes_argument_is_yes(self):
        """正常
        Yesが渡された場合、Trueが返却されること
        """
        for argument in Event.YES_LIST:
            answer = Event.is_yes(argument)

            assert answer is True

    def test_is_yes_argument_is_not_yes(self):
        """正常
        Yes以外が渡された場合、Falseが返却されること
        """
        not_yes_list = ['', 'n', 'no', 'o', 'N', 'i', 'の', 'いいえ']
        for argument in not_yes_list:
            answer = Event.is_yes(argument)

            assert answer is False
