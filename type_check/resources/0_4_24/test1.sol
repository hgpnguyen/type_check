pragma solidity ^0.4.24;
contract MyContract {
    function add() public pure returns (uint) {
        (uint a, uint j, ) = (5, 10, 22);
        uint b = 4;
        uint i = a + b;
        a = b + 5;
        b = 5 + 6;
        return i;
    }
}