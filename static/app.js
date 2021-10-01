// static/app.js

import { ethers } from './ethers.min.js';
import Crowdfunding from './abi/Crowdfunding.js';
import VeuButton from './components/VeuButton.js';
import VeuInput from './components/VeuInput.js';
import VeuPane from './components/VeuPane.js';

const privKey = '0x7151b111a8f134a03f53f1eecba97507ddaa55f2dbe91296f7faa3705541c4a4'

export default {
  name: 'app',
  data: () => ({
    'ethereum': null,
    'account': '',
    'amount': 100,
    'contractAddress': '0x8eE067b5a2FB9eCD891F95aF14dae0ad80e835A7'
  }),
  components: { VeuButton, VeuInput, VeuPane },
  methods: {
    participate() {
      let vue = this;
      // Load Crowdfunding Contract
      let provider = new ethers.providers.Web3Provider(vue.ethereum, "any");
      let signer = provider.getSigner();
      let contract = new ethers.Contract(vue.contractAddress, Crowdfunding.abi, signer);
      contract.functions.participate()
        .then((resp) => {
          console.log(resp);
        })
    }
  },
  mounted() {
    let vue = this;
    if (window.ethereum) {
      vue.ethereum = window.ethereum;
      // Load User Account
      vue.ethereum
        .request({ method: 'eth_requestAccounts' })
        .then((accounts) => {
          if (!!accounts) {
            console.log(accounts);
            vue.account = accounts[0];
          }
        }).catch(console.error);
    }
  },
  template: `
    <veu-pane class='dark container'>
      <br />
      <div class='row align-center'>
        <img src='/static/images/lambo.jpg'>
      </div>
      <br />
      <div class='row align-center'>
        Help Sitt get a Lambo
      </div>
      <br />
      <div class='row align-center'>
        Hello, {{ account }}
      </div>
      <br />
      <div class='row'>
        <div class='col-20'></div>
        <div class='col-20'></div>
        <div class='col-20'>
          <veu-input :val='amount' @update:val='amount=$event'/>
        </div>
      </div>
      <br />
      <div class='row align-center'>
        <veu-button :text='"Participate"' @click.prevent='participate()'/>
      </div>
    </veu-pane>
  `
};