pragma solidity ^0.5.0;
contract MyContract {
    function tuple() public pure returns (uint a, uint b, uint c){
        return (10, 5, 6);
    }
    function add() public pure returns (uint) {
        uint a = 3;
        uint b = 4;
        uint j;
        a += b;
        b += 6;
        (a, b) = (b + 5, a + j);
        (a, b, ) = tuple();
        (uint c, uint d, ) = tuple();
        return a;
    }
}