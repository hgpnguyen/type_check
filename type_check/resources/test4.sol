pragma solidity ^0.5.0;
contract MyContract {
    function add() public pure returns (uint) {
        uint8 a = 3;
        uint b = 4;
        uint16 c = 25;
        uint i = a + b;
        b = c + a;
        return a;
    }
}