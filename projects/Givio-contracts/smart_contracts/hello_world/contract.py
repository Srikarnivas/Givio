
from algopy import *
from algopy.arc4 import abimethod



contract Crowdfunding {
    string public name;
    string public description;
    uint256 public goal;
    uint256 public deadline;
    address public owner;
    bool public paused;

    enum CampaignState { Active, Successful, Failed }
    CampaignState public state;

    struct Tier {
        string name;
        uint256 amount;
        uint256 backers;
    }
    struct Backer {
        uint256 totalContribution;
        mapping(uint256 => bool) fundedTiers;
    }
    Tier[] public tiers;
    mapping(address => Backer) public backers;
