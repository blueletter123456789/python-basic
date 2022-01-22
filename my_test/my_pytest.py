import pytest

from my_test import calculation

# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) != 4
is_skip = True


# pytest -rs -s my_pytest.py
class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('setup class')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('teardown class')
        del cls.cal

    def setup_method(self, method):
        print('setup {}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('teardown {}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skipif(not is_skip, reason='skip!')
    @pytest.mark.skip(reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
