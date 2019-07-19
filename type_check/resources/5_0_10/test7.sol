pragma solidity ^0.5.0;

contract A {
    address payable owner;
    uint private x;
    constructor(uint a) public payable {
        x = a;
    }

    function  f() public pure returns (uint b){
        return 5 * 6;
    }

}

contract MyContract {
    A contractA = new A(5);
    function add() public pure returns (uint) {
        uint i;
        int f;
        int g = 10;
        uint len;
        return i;
    }
}