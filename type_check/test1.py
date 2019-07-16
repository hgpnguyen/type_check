import unittest
from type_check import *


class Test_test1(unittest.TestCase):
    def test_1(self):
        ast = loadJson("resources/test1.sol_json.ast")
        add_opp = jsonSearch(ast, assign_search)
        expected = [['105:32:0', 'uint256', 'int_const 5'], ['105:32:0', 'uint256', 'int_const 10'],
                   ['148:10:0', 'uint256', 'int_const 4'], ['169:14:0', 'uint256', 'uint256', 'uint256'], 
                   ['194:9:0', 'uint256', 'uint256', 'int_const 5'], ['214:9:0', 'uint256', 'int_const 5', 'int_const 6']]
        self.assertEqual(print_result(add_opp), expected)
        return;

if __name__ == '__main__':
    unittest.main()
