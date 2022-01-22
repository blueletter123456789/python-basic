import unittest

import calculation

skip_type = 'dev'


class CalTest(unittest.TestCase):
    def setUp(self) -> None:
        print('set up')
        self.cal = calculation.Cal()

    def tearDown(self) -> None:
        print('tear down')
        del self.cal

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    # @unittest.skip('it will skip!')
    @unittest.skipIf(skip_type == 'dev', 'skip!')
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
