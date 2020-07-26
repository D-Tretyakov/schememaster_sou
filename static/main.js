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
    select1: [
      {value:'c1-v1', text:'Физическое лицо'},
      {value:'c1-v2', text:'Юридическое лицо'},
      {value:'c1-v3', text:'Государственный орган (орган местного самоуправления)'},
      {value:'c1-v4', text:'Индивидуальный предприниматель'},
    ],
    choice2: [
      {val: "c2-v3"}
    ],
    select2: [
      {value:'c2-v3', text:'Физическое лицо'},
      {value:'c2-v4', text:'Юридическое лицо'},
      {value:'c2-v5', text:'Государственный орган (орган местного самоуправления)'},
      {value:'c2-v6', text:'Индивидуальный предприниматель'},
    ],
    choice3: [
      {val: "c3-v1"}
    ],
    select3: [
      {value:'c3-v1', text:'Физическое лицо'},
      {value:'c3-v2', text:'Юридическое лицо'},
      {value:'c3-v3', text:'Государственный орган (орган местного самоуправления)'},
      {value:'c3-v4', text:'Индивидуальный предприниматель'},
    ],
    choice4: [
      {val: "c4-v3"}
    ],
    select4: [
      {value:'c4-v3', text:'Физическое лицо'},
      {value:'c4-v4', text:'Юридическое лицо'},
      {value:'c4-v5', text:'Государственный орган (орган местного самоуправления)'},
      {value:'c4-v6', text:'Индивидуальный предприниматель'},
    ],
    choice5: "c5-v1",
    choice6: "c6-v1",
    choice61: [],
    choice7: ["c7-v1"],
    show_opt1: false,
    show_opt23: false,
    show_opt4: false,
    choice7options: [
      {option1: ''},
      {option2: ''},
      {option3: ''},
      {option4: ''},
    ],
    // choice71: "c7-v9",
    choice8: ["c8-v1"],
    choice9: "c9-v1",
    choice10: "c10-v1",
    choice11: "c11-v1",
    needs_tax: true,
    needs_price_7: true,
    about_possesions: true,
    needs_price_8: true,

    download_available: false,

    updating: false,
    error: false,
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
    // check: function (node_id) { 
    //   const index = this.choice7.indexOf(node_id)
    //   if (index == -1) {
    //     this.choice7.push(node_id)
    //   }
    // },
    // uncheck: function(node_id) {
    //   const index = this.choice7.indexOf(node_id)
    //   if (index > -1) {
    //     this.choice7.splice(index, 1)
    //   }
    //   document.getElementById('c7-block1').style.display = 'none'
    // },
    onChange1() {
      this.needs_tax = true
      for (let i = 0; i < this.choice1.length; i++) {
        if (this.choice1[i].val === 'c1-v3') {
          this.needs_tax = false
          this.choice6 = 'c6-v29'
        }
      }
    },
    onChange2() {
      var show = false
      for (let i = 0; i < this.choice2.length; i++) {
        if (this.choice2[i].val === 'c2-v3') {
          show = true;
        }
      }
      // console.log(show)
      if (show) {
        document.getElementById('c2-h1').style.display = ''
      } else {
        document.getElementById('c2-h1').style.display = 'none'
      }
    },
    onChange7() {
      if (this.choice7.includes('c7-v2')) {
        document.getElementById('c7-h1').style.display = ''
      } else {
        document.getElementById('c7-h1').style.display = 'none'
      }

      if (this.choice7.includes('c7-v15')) {
        document.getElementById('c7-h2').style.display = ''
      } else {
        document.getElementById('c7-h2').style.display = 'none'
      }

      if (this.choice7.includes('c7-v16')) {
        document.getElementById('c7-h3').style.display = ''
      } else {
        document.getElementById('c7-h3').style.display = 'none'
      }

      if (this.choice7.includes('c7-v20')) {
        document.getElementById('c7-h4').style.display = ''
      } else {
        document.getElementById('c7-h4').style.display = 'none'
      }

      // if (['c7-v1','c7-v2','c7-v3',
      //      'c7-v4','c7-v5','c7-v6',
      //      'c7-v7','c7-v7','c7-v9',
      //      'c7-v10','c7-v11','c7-v12',
      //      'c7-v13','c7-v14','c7-v15', 'c7-v24',
      //     ].includes(this.choice7)) {
      if (this.choice7.some(el => 
          ['c7-v1','c7-v2','c7-v3',
           'c7-v4','c7-v5','c7-v6',
           'c7-v7','c7-v7','c7-v9',
           'c7-v10','c7-v11','c7-v12',
           'c7-v13','c7-v14','c7-v15', 
           'c7-v17', 'c7-v18', 'c7-v24',
          ].includes(el))) {
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
      if (this.choice7.includes('c8-v1')) {
        document.getElementById('c8-h1').style.display = ''
      } else {
        document.getElementById('c8-h1').style.display = 'none'
      }


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
    // ask: function () {
    //   alert(pdfjsLib)
    //   // Template.show().then(response => {
    //   //   this.api_resp = response.text
    //   //   console.log(this.api_resp)
    //   // })
    // },

    showPDF: function() {
      getPDF()
    },

    closeUpdateAlarm: function() {
      console.log('CLOSE');
      this.updating = false
    },

    updatePDF: function() {
      if (!this.download_available) {
        this.download_available = true
      }

      document.getElementById('pdf-container')
              .addEventListener('DOMSubtreeModified', this.closeUpdateAlarm);

      this.updating = true
      f = document.forms[1]
      var bodyFormData = new FormData(f)
      bodyFormData.delete('c7-block1-radio')
      bodyFormData.delete('choice-61')
      axios({
        method: 'post',
        url: document.URL + 'front/',
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
        app.updating = false
        app.error = true
        alert('Что-то пошло не так ¯\\_(ツ)_/¯')
        console.log(response)
      });
    },

    download: function() {
      window.location.href="download-doc/"
    },

    prepare: function() {
      document.getElementById('c2-v1').click()
      document.getElementById('c4-v1').click()
    }

  },
  mounted: function(){
    document.getElementById('app')
            .addEventListener('DOMSubtreeModified', this.prepare);
  },
})
