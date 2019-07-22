pragma solidity ^0.4.24;
contract MyContract {
    uint16[] b;
    mapping(uint16 => uint16) map;
    enum ActionChoices { GoLeft, GoRight, GoStraight, SitStill }
    ActionChoices choice;
    ActionChoices constant defaultChoice = ActionChoices.GoStraight;

    function f(uint80 a, uint160 c) public pure returns(uint160) {
        return a + c;
    }

    function add() public returns (uint) {
        uint a = 3;
        b.push(1);
        uint i = a + b[0];
        uint d = 5 + map[10];
        uint z = b[0] + this.f(10, 100);

        return i;
    }
}