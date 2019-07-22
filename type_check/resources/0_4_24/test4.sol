pragma solidity ^0.4.24;
contract MyContract {
    address addr;
    mapping(uint => mapping(uint => bool)) map;

    function add() public pure returns (uint) {
        uint8 a = 3;
        uint b = 4;
        uint16 c = 25;
        uint i = a + b;
        bytes16 g;
        bytes8 h;
        b = c + a;
        return a;
    }
}