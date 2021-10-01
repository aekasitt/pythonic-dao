#!/usr/bin/env python3.7
# coding:utf-8
# Copyright (C) 2019-2021 All rights reserved.
# FILENAME:  generate-mnemonic.py
# VERSION: 	 1.0
# CREATED: 	 2021-09-30 12:11
# AUTHOR: 	 Sitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION: Manual Script to create a Mnemonic Passphrase
#
# HISTORY:
#*************************************************************
### Standard Packages ###
from argparse import ArgumentParser
### Third-Party Packages ###
from bip_utils import ( Bip39MnemonicGenerator, Bip39WordsNum )
from brownie import accounts
from yaml import dump

def main():
  parser = ArgumentParser()
  parser.add_argument('num', type=int, nargs='?', default=12, help='Word Number')
  parser.add_argument('--filename', '-fn', default='wallet', help='Filename (.yml) to save mnemonic')
  parser.add_argument('--force', '-f', action='store_true', help='Force override ganache.yml if exists')
  args = parser.parse_args()
  yaml_exists = False
  try:
    with open(f'{args.filename}.yml', 'rb') as f:
      print(f.read())
      yaml_exists = True
  except FileNotFoundError: pass

  print(f'File-Exists: {yaml_exists}')
  # Generate a random mnemonic string of 15 words
  word_name_map = {
    12: Bip39WordsNum.WORDS_NUM_12,
    15: Bip39WordsNum.WORDS_NUM_15
  }
  words_num = word_name_map.get(args.num, Bip39WordsNum.WORDS_NUM_12)
  print(f'Word Count: {words_num}')
  mnemonic = Bip39MnemonicGenerator().FromWordsNumber(words_num)
  print(f'Mnemonic: {mnemonic}')
  account = accounts.from_mnemonic(mnemonic, count=1)
  print(f'Wallet Address: {account.address}')
  if yaml_exists and not args.force:
    print('!! YAML file already exists; To override, run with `--force` flag')
  else:
    with open(f'{args.filename}.yml', 'w') as f:
      content = { 'mnemonic': mnemonic, 'privkey': account.private_key }
      dump(content, f)

if __name__ == '__main__':
  main()
