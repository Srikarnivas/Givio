from email.headerregistry import Address
from algopy import *
from algopy.arc4 import abimethod



class Donation(ARC4Contract):
    creator_address : Account
    total_donations : BigUInt
    target : BigUInt
    campaign_active: bool

    @abimethod(allow_actions=["NoOp"], create="require")
    def create(self, target: BigUInt, status: bool) -> None:
        assert target > 0
        self.creator_address = Txn.sender
        self.total_donations = 0
        self.target = target
        self.campaign_active = status

    @abimethod()
    def toggle_campaign(self, status: bool) -> None:
        assert Txn.sender == self.creator_address
        self.campaign_active = status

    @abimethod()
    def get_campaign_details(self) -> tuple[Account, BigUInt, BigUInt, bool]:
        return self.creator_address, self.total_donations, self.target, self.campaign_active


    @abimethod()
    def is_target_reached(self) -> bool:
        return self.total_donations == self.target

    @abimethod()
    def donate(self, donateTxn: gtxn.PaymentTransaction ) -> None:
        assert self.campaign_active
        assert donateTxn.sender == Txn.sender
        assert donateTxn.receiver == Global.current_application_address
        assert donateTxn.amount > 0
        assert self.total_donations+donateTxn.amount <= self.target

        self.total_donations += donateTxn.amount


