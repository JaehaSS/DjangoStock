import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home";
import About from "./views/About";
import Signup from "./views/signup";
import Chart from "./views/Chart";
import CandleChart from "./views/CandleChart";
import Login from "./views/login";



Vue.use(VueRouter);


const router = new VueRouter({
  mode : "history",
  routes : [
    {path:"/", component: Home, name: 'Home'},
    {path:"/about", component: About, name: 'about'},
    {path:"/signup", component: Signup, name: 'Signup'},
    {path:"/chart", component: Chart, name: 'Chart'},
    {path:"/CandleChart", component: CandleChart, name: 'CandleChart'},
    {path:"/login", component: Login, name: 'login'},
  ]
});


// const router = new VueRouter({
//     mode: "history",
//     routes: [{
//         path: "/",
//         component: Home
//       },
//       {
//         path: "/about",
//         component: About
//       }
//     ]
//   });

export default router;
