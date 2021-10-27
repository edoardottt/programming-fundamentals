import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):
    def do_test(self, tabella, column, expected, expectedTab):
        """Test implementation
        - table       : table in the form of a list of dictionaries
        - column       : table column name
        - expected      : expected number of columns
        - expectedTab   : modified waiting table
        """
        with self.ignored_function("builtins.print"), self.forbidden_function(
            "os.walk"
        ), self.timer(2):
            result = program.es26(table, column)
        self.assertEqual(
            result, expected, f "The result must be {expected} instead of {result}"
        )
        self.assertEqual(
            table,
            expectedTab,
            f "The result must be {expectedTab} instead of {table}",
        )

    @data(
        (
            [
                {"C1": 2, "C2": 1, "C3": "d"},
                {"C1": 4, "C2": 7, "C3": "a"},
                {"C1": 6, "C2": 1, "C3": "b"},
                {"C1": 8, "C2": 3, "C3": "c"},
            ],
            "C1",
            3,
            [
                {"C1": 8, "C2": 3, "C3": "c"},
                {"C1": 6, "C2": 1, "C3": "b"},
                {"C1": 4, "C2": 7, "C3": "a"},
                {"C1": 2, "C2": 1, "C3": "d"},
            ],
        ),
        (
            [
                {"C1": 2, "C2": 1, "C3": "d"},
                {"C1": 4, "C2": 7, "C3": "a"},
                {"C1": 6, "C2": 1, "C3": "b"},
                {"C1": 8, "C2": 3, "C3": "c"},
            ],
            "C3",
            3,
            [
                {"C1": 2, "C2": 1, "C3": "d"},
                {"C1": 8, "C2": 3, "C3": "c"},
                {"C1": 6, "C2": 1, "C3": "b"},
                {"C1": 4, "C2": 7, "C3": "a"},
            ],
        ),
    )
    @unpack
    def test(self, tabella, column, expected, expectedTab):
        return self.do_test(table, column, expected, expectedTab)


# TESTS ARE PERFORMED BOTH BY RUNNING program.py and by calling pytest in the directory
if __name__ == "__main__":
    Test.main()
