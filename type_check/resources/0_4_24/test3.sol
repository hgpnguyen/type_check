pragma solidity ^0.4.24;
contract MyContract {
    address addr;
    mapping(uint => uint8) ma;

    function add() public pure returns (uint) {
        uint16 c = 3;
        uint8 b = 4;
        uint a = (b + c) * 10;
        string memory str;
        bool k;
        int8 g;
        b++;
        a = ++b;
        return a;
    }
}