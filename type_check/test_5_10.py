import unittest
from type_check import *


class Test_test_5_10(unittest.TestCase):
    def test_1(self):
        ast = loadJson("resources/5_0_10/test1.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[7, 'a', 'uint256'], [9, 'j', 'uint256'], [16, 'b', 'uint256'], [20, 'i', 'uint256']] 
        self.assertEqual(get_var_Type(add_opp), expected)

    def test_2(self):
        ast = loadJson("resources/5_0_10/test2.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[4, 'a', 'uint256'], [6, 'b', 'uint256'], [8, 'c', 'uint256'], [22, 'a', 'uint256'], 
                    [26, 'b', 'uint256'], [30, 'j', 'uint256'], [60, 'c', 'uint256'], [62, 'd', 'uint256']]
        self.assertEqual(get_var_Type(add_opp), expected)

    def test_3(self):
        ast = loadJson("resources/5_0_10/test3.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[3, 'addr', 'address'], [7, 'ma', 'mapping(uint256 => uint8)'], [13, 'c', 'uint16'], 
                    [17, 'b', 'uint8'], [21, 'a', 'uint256'], [30, 'str', 'string'], 
                    [33, 'k', 'bool'], [36, 'g', 'int8']]
        self.assertEqual(get_var_Type(add_opp), expected)

    def test_4(self):
        ast = loadJson("resources/5_0_10/test4.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[3, 'addr', 'address payable'], [9, 'map', 'mapping(uint256 => mapping(uint256 => bool))'], 
                    [15, 'a', 'uint8'], [19, 'b', 'uint256'], [23, 'c', 'uint16'], 
                    [27, 'i', 'uint256'], [33, 'g', 'bytes16'], [36, 'h', 'bytes8']]
        self.assertEqual(get_var_Type(add_opp), expected)

    def test_5_enum(self):
        ast = loadJson("resources/5_0_10/test5.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[4, 'b', 'uint16[]'], [8, 'map', 'mapping(uint16 => uint16)'], 
                    [15, 'choice', 'enum MyContract.ActionChoices'], [19, 'defaultChoice', 'enum MyContract.ActionChoices'], 
                    [21, 'a', 'uint80'], [23, 'c', 'uint160'], [39, 'a', 'uint256'], 
                    [49, 'i', 'uint256'], [57, 'd', 'uint256'], [65, 'z', 'uint256']]
        self.assertEqual(get_var_Type(add_opp), expected)

    def test_6_array(self):
        ast = loadJson("resources/5_0_10/test6.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[7, 'i', 'uint256'], [10, 'f', 'int256'], [13, 'g', 'int256'], 
                    [17, 'len', 'uint256'], [22, 'a', 'uint256[]'], [30, 'b', 'bytes']]
        self.assertEqual(get_var_Type(add_opp), expected)
        
    def test_7_contract(self):
        ast = loadJson("resources/5_0_10/test7.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[3, 'owner', 'address payable'], [5, 'x', 'uint256'], [7, 'a', 'uint256'], 
                    [18, 'b', 'uint256'], [32, 'contractA', 'contract A'], 
                    [38, 'i', 'uint256'], [41, 'f', 'int256'], [44, 'g', 'int256'], [48, 'len', 'uint256']]
        self.assertEqual(get_var_Type(add_opp), expected)

    def test_8_struct(self):
        ast = loadJson("resources/5_0_10/test8.sol_json.ast")
        add_opp = jsonSearch(ast, variable_search)
        expected = [[4, 'contents', 'uint256[]'], [6, 'moreInfo', 'uint256'], [9, 's', 'struct MyContract.StructType'], 
                    [15, 'i', 'uint256'], [18, 'f', 'int256'], [21, 'g', 'int256'], [25, 'len', 'uint256']]
        self.assertEqual(get_var_Type(add_opp), expected)


if __name__ == '__main__':
    unittest.main()
