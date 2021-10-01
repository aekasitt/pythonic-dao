# @version ^0.2.7
'''
@title Crowdfunding Contract
@author Sitt Guruvanich
@license MiT
@notice
  The crowdfunding contract is able to add new tokens to be withdrawn
  once the timelock period is over
'''

### Structs & Interfaces ###
struct Patron:
  addr: address
  amount: uint256

### Public Vars ###
deadline:  public(uint256)
timelimit: public(uint256)
goal:      public(uint256)
### Private Vars ###
admin:         address
beneficiary:   address
patrons:       HashMap[int128, Patron]
nextPatronIdx: int128 
refundIndex:   int128

### Constants ###
### Events ###
event OwnershipTransferred:
  previousOwner: address
  newOwner: address

### Constructor ###
@external
def __init__(_beneficiary: address, _goal: uint256, _timelimit: uint256):
  assert _beneficiary != ZERO_ADDRESS # dev: beneficiary address cannot be null
  assert _goal        != 0 # dev: goal cannot be zero
  assert _timelimit   != 0 # dev: timelimit cannot be zero
  self.beneficiary     = _beneficiary
  self.goal            = _goal
  self.deadline        = block.timestamp + _timelimit
  self.timelimit       = _timelimit

### Participate in this crowdfunding campaign ###
@external
@payable
def participate():
  assert block.timestamp  < self.deadline, 'Crowdfunding deadline hasn\'t passed' # dev: too early
  patronIdx: int128       = self.nextPatronIdx
  self.patrons[patronIdx] = Patron({addr: msg.sender, amount: msg.value})
  self.nextPatronIdx      = patronIdx + 1

### Finalized by Admin ###
@external
def finalize():
  assert msg.sender == self.admin, 'This method is restricted for admin only'  # dev: admin only
  assert self.balance >= self.goal, 'The goal has been reached'
  selfdestruct(self.beneficiary)

# Not enough money was raised! Refund everyone (max 30 people at a time
# to avoid gas limit issues)
@external
def refund():
  assert block.timestamp >= self.deadline and self.balance < self.goal
  idx: int128 = self.refundIndex
  for i in range(idx, idx + 30):
    if i >= self.nextPatronIdx:
      self.refundIndex = self.nextPatronIdx
      return
    send(self.patrons[i].addr, self.patrons[i].amount)
    self.patrons[i]  = empty(Patron)
    self.refundIndex = idx + 30

### Contract Ownership ###
@external
def transferOwnership(_addr: address):
  '''
  @notice Transfer ownership of Crowdfunding contract to `_addr`
  @param _addr Address to have ownership transferred to
  '''
  assert msg.sender == self.admin, 'This method is restricted for admin only'  # dev: admin only
  assert _addr      != ZERO_ADDRESS, 'New admin address cannot be null'  # dev: admin not set
  _prev: address     = self.admin
  self.admin         = _addr
  log OwnershipTransferred(_prev, _addr)
