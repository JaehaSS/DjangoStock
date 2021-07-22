import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home";
import About from "./views/About";
import signup from "./views/signup";


Vue.use(VueRouter);


const router = new VueRouter({
  mode : "history",
  routes : [
    {path:"/", component: Home, name: 'Home'},
    {path:"/about", component: About, name: 'about'},
    {path:"/signup", component: signup, name: 'signup'},
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
