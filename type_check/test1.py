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

    def test_tupple(self):
        ast = loadJson("resources/test2.sol_json.ast")
        add_opp = jsonSearch(ast, assign_search)
        expected = [['208:10:0', 'uint256', 'int_const 3'], ['229:10:0', 'uint256', 'int_const 4'], ['267:6:0', 'uint256', 'uint256'], ['284:6:0', 'uint256', 'int_const 6'], 
                   ['301:23:0', 'uint256', 'uint256', 'int_const 5'], ['301:23:0', 'uint256', 'uint256', 'uint256'], ['335:18:0', 'uint256', 'tuple(uint256,uint256,uint256)'],
                   ['335:18:0', 'uint256', 'tuple(uint256,uint256,uint256)'], ['364:28:0', 'uint256', 'tuple(uint256,uint256,uint256)'],
                   ['364:28:0', 'uint256', 'tuple(uint256,uint256,uint256)']]
        self.assertEqual(print_result(add_opp), expected)
        return;

    def test_4(self):
        ast = loadJson("resources/test4.sol_json.ast")
        add_opp = jsonSearch(ast, assign_search)
        expected = [['105:11:0', 'uint8', 'int_const 3'], ['127:10:0', 'uint256', 'int_const 4'], ['148:13:0', 'uint16', 'int_const 25'], 
                    ['172:14:0', 'uint256', 'uint8', 'uint256'], 
                    ['197:9:0', 'uint256', 'uint16', 'uint8']]
        self.assertEqual(print_result(add_opp), expected)
        return;

    def test_other_exp(self):
        ast = loadJson("resources/test5.sol_json.ast")
        add_opp = jsonSearch(ast, assign_search)
        expected = [['255:10:0', 'uint256', 'int_const 3'], ['296:17:0', 'uint256', 'uint256', 'uint16'], 
                    ['324:20:0', 'uint256', 'int_const 5', 'uint16'], ['355:31:0', 'uint256', 'uint16', 'uint160']]
        self.assertEqual(print_result(add_opp), expected)
        return;

    def test_6(self):
        ast = loadJson("resources/test6.sol_json.ast")
        add_opp = jsonSearch(ast, assign_search)
        expected = [['105:12:0', 'uint256', 'int_const 150'], ['128:13:0', 'uint8', 'int_const 150'], 
                    ['152:14:0', 'uint256', 'uint256', 'uint8'], ['193:10:0', 'int256', 'int_const 10'], ['214:14:0', 'int256', 'uint8', 'int_const 150'], 
                    ['239:22:0', 'uint256', 'uint8', 'int_const 2', 'uint256', 'int_const 4'], 
                    ['272:14:0', 'uint256', 'uint256', 'uint8', 'int_const 10']]
        self.assertEqual(print_result(add_opp), expected)
        return;

if __name__ == '__main__':
    unittest.main()
