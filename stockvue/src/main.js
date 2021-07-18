import Vue from 'vue';
import App from './App.vue';
import router from "./router"
import axios from "axios";

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue' // vue bootstrap 쓰기 위한 부분
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


new Vue({
  router,
  render: h => h(App),
}).$mount('#app');





let url = "http://localhost:8000/app1/api/tutorials"; // 장고 서버 주소

axios.get(url)
.then(function(response){
  console.log(response);
})
.catch(function(response){
  console.log(response);
})