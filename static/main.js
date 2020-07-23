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
    choice0: "c0-v1",
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
    choice71: "c7-v9",
    choice8: ["c8-v1"],
    choice9: "c9-v1",
    choice10: "c10-v1",
    choice11: "c11-v1",
    needs_tax: true,
    needs_price_7: true,
    needs_price_8: true,
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
    onChange7() {
      if (['c7-v1','c7-v2','c7-v3',
           'c7-v4','c7-v5','c7-v6',
           'c7-v7','c7-v7','c7-v9',
           'c7-v10','c7-v11','c7-v12',
           'c7-v13','c7-v14','c7-v15', 'c7-v24',
          ].includes(this.choice7)) {
        // this.choice5 = 'c5-v1'
        // document.getElementById('c5-v1').click()
        // document.getElementById('c5-v1').disabled = true
        this.needs_price_7 = true;
      } else {
        // this.choice5 = 'c5-v2'
        // document.getElementById('c5-v2').click()
        // document.getElementById('c5-v2').disabled = true
        this.needs_price_7 = false;
      }

      if (this.needs_price_7 || this.needs_price_8) {
        this.choice5 = 'c5-v1'
        document.getElementById('c5-v1').click()
        // document.getElementById('c5-v1').disabled = true
        // document.getElementById('c5-v2').disabled = true
      } else {
        this.choice5 = 'c5-v2'
        document.getElementById('c5-v2').click()
        // document.getElementById('c5-v1').disabled = true
        // document.getElementById('c5-v2').disabled = true
      }

      console.log('NEEDS PRICE?')
      console.log(this.needs_price_7 || this.needs_price_8)
    },
    onChange8() {
      if (this.choice8.length == 1 && this.choice8[0] == 'c8-v3') {
        this.needs_price_8 = false;
      } else {
        this.needs_price_8 = true;
      }

      if (this.needs_price_7 || this.needs_price_8) {
        this.choice5 = 'c5-v1'
        // document.getElementById('c5-v1').disabled = false
        // document.getElementById('c5-v2').disabled = false
        document.getElementById('c5-v1').click()
        // document.getElementById('c5-v1').disabled = true
        // document.getElementById('c5-v2').disabled = true
      } else {
        this.choice5 = 'c5-v2'
        // document.getElementById('c5-v1').disabled = false
        // document.getElementById('c5-v2').disabled = false
        document.getElementById('c5-v2').click()
        // document.getElementById('c5-v1').disabled = true
        // document.getElementById('c5-v2').disabled = true
      }

      console.log('NEEDS PRICE?')
      console.log(this.needs_price_7 || this.needs_price_8)
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
      alert(pdfjsLib)
      // Template.show().then(response => {
      //   this.api_resp = response.text
      //   console.log(this.api_resp)
      // })
    },

    showPDF: function() {
      getPDF()
    },

    updatePDF: function() {
      f = document.forms[0]
      var bodyFormData = new FormData(f)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/schemegen/front/',
        data: bodyFormData,
        headers: {'Content-Type': 'multipart/form-data' }
        })
        .then(function (response) {
            //handle success
            console.log(response)
            getPDF()
        })
        .catch(function (response) {
            //handle error
            console.log(response)
        });
    }
  }
})
