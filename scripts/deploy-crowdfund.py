#!/usr/bin/env python3.7
# coding:utf-8
# Copyright (C) 2019-2021 All rights reserved.
# FILENAME:  deploy-crowdfund.py
# VERSION: 	 1.0
# CREATED: 	 2021-09-30 13:40
# AUTHOR: 	 Aekasitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
### Standard Packages ###
from yaml import safe_load
### Project Contract(s) ###
from brownie import Crowdfunding
### Third-Party Packages ###
from brownie.convert import Wei
from brownie.network import accounts, Chain
from eth_account.account import Account, ValidationError

TERM_RED  = '\033[1;31m'
TERM_NFMT = '\033[0;0m'

def main(gas_speed: str = 'standard'):
  ### Load Account to use ###
  admin: Account       = None
  beneficiary: Account = None
  chain: Chain         = Chain()
  print(f'Network Chain-ID: { chain }')
  admin_addr_map: dict = {
    1: None,                # mainnet
    42: 'admin-ropsten',    # kovan testnet
    1337: 'admin',          # local EVM
    10001: 'admin-smartbch' # smartbch
  }
  benef_addr_map: dict = {
    1: None,                      # mainnet
    42: 'beneficiary-ropsten',    # ropsten
    1337: 'beneficiary',          # local EVM
    10001: 'beneficiary-smartbch' # smartbch
  }

  if chain._chainid in (1, 42, 1337, 10001):
    admin_suffix: str = admin_addr_map[chain._chainid]
    benef_suffix: str = benef_addr_map[chain._chainid]
    admin_yaml: str = 'wallet.yml' if admin_suffix is None else f'wallet.{admin_suffix}.yml'
    benef_yaml: str = 'wallet.yml' if benef_suffix is None else f'wallet.{benef_suffix}.yml'
    ### Load Mnemonic from YAML File ###
    try:
      with open(admin_yaml) as f:
        content  = safe_load(f)
        mnemonic = content.get('mnemonic', None)
        admin    = accounts.from_mnemonic(mnemonic, count=1)
      with open(benef_yaml) as f:
        content     = safe_load(f)
        mnemonic    = content.get('mnemonic', None)
        beneficiary = accounts.from_mnemonic(mnemonic, count=1)
    except FileNotFoundError:
      print(f'{ TERM_RED }Cannot find wallet mnemonic file(s).{ TERM_NFMT }')
      return
    except ValidationError:
      print(f'{ TERM_RED }Invalid address found in wallet mnemonic file.{ TERM_NFMT }')
      return
  else:
    print(f'{ TERM_RED }Invalid chainid found. { TERM_NFMT }')
    return
  for i, acct in enumerate([ admin, beneficiary ]):
    print(f'Account {i}: {acct}')
    if chain._chainid == 1337: 
      try:
        accounts[i].transfer(acct, Wei('100 ether').to('wei'))
      except ValueError: pass
    balance = acct.balance()
    print(f'Account Balance: {balance}')
    if balance == 0:
      return # If balance is zero, exits
  cf = Crowdfunding.deploy(beneficiary, Wei('10 ether'), 10, {'from':  admin})
  del admin_addr_map, benef_addr_map
