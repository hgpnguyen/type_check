pragma solidity ^0.5.0;
contract MyContract {
    function add() public pure returns (uint) {
        uint a = 3;
        uint b = 4;
        uint i = a + b;
        return i;
    }
}