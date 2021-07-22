import Vue from 'vue';
import App from './App.vue';
import router from "./router"
import axios from "axios";
import vuetify from './plugins/vuetify'
import VeeValidate from 'vee-validate';

Vue.config.productionTip = false

new Vue({
  VeeValidate,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');





// let url = "http://localhost:8000/app1/api/tutorials"; // 장고 서버 주소

// axios.get(url)
//   .then(function(response){
//     console.log(response);
//   })
//   .catch(function(response){
//     console.log(response);
//   })
