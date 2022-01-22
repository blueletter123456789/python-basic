import os
import pytest
from my_test import calculation


class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()
        cls.file_name = 'test.txt'

    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.file_name)
        test_file_path = os.path.join(tmpdir, self.file_name)
        # assert os.path.exists(test_file_path)
        with open(test_file_path, 'r') as f:
            text = f.read()
        assert text == 'test'
