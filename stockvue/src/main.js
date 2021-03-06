import Vue from 'vue';
import App from './App.vue';
import router from "./router"
import axios from "axios";
import vuetify from './plugins/vuetify'
import VeeValidate from 'vee-validate';
import VueApexCharts from 'vue-apexcharts'
import store from "./store"
import 'es6-promise/auto'
import AxiosPlugin from 'vue-axios-cors'

Vue.use(AxiosPlugin);
Vue.use(VueApexCharts)
Vue.config.productionTip = false
Vue.component('apexchart', VueApexCharts)
// axios.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded'
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
Vue.prototype.$axios = axios; //전역변수로 설정 컴포넌트에서 this.$axios 호출할 수 있음

// axios.defaults.headers.get['header-name'] = 'value'




new Vue({
  VeeValidate,
  store,
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
