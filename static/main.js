// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// import Vue from 'vue'
// import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.esm.browser.js'
// import App from './App'

// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)

// import { Template } from './api/demo'


Vue.config.productionTip = false

// Vue.component('hint', {
//   props: ['text', '_href'],
//   template: '<p>{{ text }} <a :href="_href">click</a></p>'
// })

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   components: { App },
//   template: '<App/>'
// })
var app = new Vue({
  el: '#app',
  data: {
    choice0: ["c0-v1"],
    // choice1: "c1-v1",
    choice1: [
      {val: "c1-v1"}
    ],
    choice2: [
      {val: "c2-v3"}
    ],
    choice3: [
      {val: "c3-v1"}
    ],
    choice4: [
      {val: "c4-v3"}
    ],
    choice5: "c5-v1",
    choice6: "c6-v1",
    choice7: "c7-v1",
    choice8: ["c8-v1"],
    choice9: "c9-v1",
    choice10: "c10-v1",
    choice11: "c11-v1",
    needs_tax: true,
    api_resp: '',
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
    click: function (node_id) {
      document.getElementById(node_id).click()
    },
    onChange1() {
      this.needs_tax = true
      for (let i = 0; i < this.choice1.length; i++) {
        if (this.choice1[i].val === 'c1-v3') {
          this.needs_tax = false
          this.choice6 = 'c6-v29'
        }
      }
    },
    send: function () {
      console.log('choice 0' + ' ' + this.choice0);
      console.log('choice 1' + ' ' + this.choice1);
      console.log('choice 2' + ' ' + this.choice2);
      console.log('choice 3' + ' ' + this.choice3);
      console.log('choice 4' + ' ' + this.choice4);
      console.log('choice 5' + ' ' + this.choice5);
      console.log('choice 6' + ' ' + this.choice6);
      console.log('choice 7' + ' ' + this.choice7);
      console.log('choice 8' + ' ' + this.choice8);
      console.log('choice 9' + ' ' + this.choice9);
      console.log('choice 10' + ' ' + this.choice10);
      console.log('choice 11' + ' ' + this.choice11);
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
