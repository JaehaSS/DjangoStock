import Vue from 'vue'
import App from './App.vue'
import axios from "axios";

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')




let url = "http://localhost:8000/admin/"; // 장고 서버 주소

axios.get(url)
.then(function(response){
  console.log(response);
})
.catch(function(response){
  console.log(response);
})