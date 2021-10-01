export default {
  'abi': [{
    'anonymous': false,
    'inputs': [
      {
        'indexed': false,
        'name': 'previousOwner',
        'type': 'address'
      },
      {
        'indexed': false,
        'name': 'newOwner',
        'type': 'address'
      }
    ],
    'name': 'OwnershipTransferred',
    'type': 'event'
  },
  {
    'inputs': [
      {
        'name': '_beneficiary',
        'type': 'address'
      },
      {
        'name': '_goal',
        'type': 'uint256'
      },
      {
        'name': '_timelimit',
        'type': 'uint256'
      }
    ],
    'outputs': [],
    'stateMutability': 'nonpayable',
    'type': 'constructor'
  },
  {
    'gas': 107388,
    'inputs': [],
    'name': 'participate',
    'outputs': [],
    'stateMutability': 'payable',
    'type': 'function'
  },
  {
    'gas': 27927,
    'inputs': [],
    'name': 'finalize',
    'outputs': [],
    'stateMutability': 'nonpayable',
    'type': 'function'
  },
  {
    'gas': 4467944,
    'inputs': [],
    'name': 'refund',
    'outputs': [],
    'stateMutability': 'nonpayable',
    'type': 'function'
  },
  {
    'gas': 39556,
    'inputs': [
      {
        'name': '_addr',
        'type': 'address'
      }
    ],
    'name': 'transferOwnership',
    'outputs': [],
    'stateMutability': 'nonpayable',
    'type': 'function'
  },
  {
    'gas': 1208,
    'inputs': [],
    'name': 'deadline',
    'outputs': [
      {
        'name': '',
        'type': 'uint256'
      }
    ],
    'stateMutability': 'view',
    'type': 'function'
  },
  {
    'gas': 1238,
    'inputs': [],
    'name': 'timelimit',
    'outputs': [
      {
        'name': '',
        'type': 'uint256'
      }
    ],
    'stateMutability': 'view',
    'type': 'function'
  },
  {
    'gas': 1268,
    'inputs': [],
    'name': 'goal',
    'outputs': [
      {
        'name': '',
        'type': 'uint256'
      }
    ],
    'stateMutability': 'view',
    'type': 'function'
  }]
};