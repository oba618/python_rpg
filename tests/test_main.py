import runpy
import main


class TestMain:
    def test_main(self):
        try:
            runpy.run_module('main', run_name='__main__')
        except OSError:
            assert True
