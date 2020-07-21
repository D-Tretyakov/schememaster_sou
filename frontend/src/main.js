// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import { Template } from './api/demo'

Vue.config.productionTip = false

Vue.component('hint', {
  props: ['text', '_href'],
  template: '<p>{{ text }} <a :href="_href">click</a></p>'
})

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   components: { App },
//   template: '<App/>'
// })
var app = new Vue({
  el: '#app',
  data: {
    choice0: "c0-v1",
    choice1: "c1-v1",
    choice2: "c2-v1",
    choice3: "c3-v1",
    choice4: "c4-v1",
    choice5: "c5-v1",
    choice6: "c6-v1",
    choice7: "c7-v1",
    choice8: "c8-v1",
    choice9: "c9-v1",
    choice10: "c10-v1",
    choice11: "c11-v1",
    api_resp: '',
    choice81: "c8-v1",
    choice82: "",
    choice83: "",
    choice84: "",
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    },
    say: function (text) {
      alert(text)
    },
    show: function (node_id) {
      document.getElementById(node_id).style.display = "";
    },
    hide: function (node_id) {
      document.getElementById(node_id).style.display = "none";
    },
    send: function () {
      console.log('choice 1' + ' ' + this.choice1);
      console.log('choice 2' + ' ' + this.choice2);
      console.log('choice 3' + ' ' + this.choice3);
      console.log('choice 4' + ' ' + this.choice4);
      console.log('choice 5' + ' ' + this.choice5);
      console.log('choice 6' + ' ' + this.choice6);
    },
    ask: function () {
      // alert('KEK')
      Template.show().then(response => {
        this.api_resp = response.text
        console.log(this.api_resp)
      })
    }
  }
})
