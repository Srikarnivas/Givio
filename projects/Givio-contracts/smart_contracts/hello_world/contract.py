
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

        itxn.Payment(
            receiver= self.creator_address,
            amount = 0,
            close_remainder_to= self.creator_address,
            fee= 1_000,
        ).submit()
