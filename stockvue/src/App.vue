<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-app-bar-nav-icon @click="drawer= !drawer" />
      <v-spacer />

      <v-btn
        href="/login"
        target="_self"
        text
        v-if="isLogin"
      >
        <span class="mr-2" @click="logout" >로그아웃</span>
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <v-btn
        href="/login"
        target="_self"
        text
        v-else
      >
        <span class="mr-2">
          로그인
          </span>
        <v-icon>mdi-account-circle-outline</v-icon>
      </v-btn>


      <v-btn
        href="/signup"
        target="_self"
        text
      >
        <span class="mr-2">회원 가입</span>
        <v-icon>mdi-account-plus</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Stocksite
          </v-list-item-title>
          <v-list-item-subtitle>
            Menu
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider />

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.to"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view />
    </v-main>
    <Footer />
  </v-app>
</template>
<script>
// import Header from './components/layout/Header'
import Footer from './components/layout/Footer.vue'
// import Content from '/components/layout/Content.vue'
import { mapState, mapActions} from "vuex";



export default {
  name: 'App',

  components: {
    // Header, Footer, Content
    Footer
  },

  data: ()=> ({
    drawer:false,
    isLogin : false,
    items: [
      { title: 'Home', icon: 'mdi-view-dashboard', to:'/' },
      { title: 'Photos', icon: 'mdi-image', to :'/about' },
      { title: 'About', icon: 'mdi-help-box', to :'/signup' },
      { title: '차트', icon: 'mdi-github', to :'/chart' },
      { title: '캔들차트', icon: 'mdi-github', to :'/Candlechart' },
      { title: '로그인', icon: 'mdi-github', to :'/login' },

    ],
    right: null,
  }),
  created:function(){
    const token = localStorage.getItem('access_token')
    if(token){
      this.isLogin = true
    }
  },
  computed: {
    ...mapState(["isLoign"])
  },
  methods: {
    ...mapActions(["logout"])
  },


};
</script>


<style>
html,body{padding:0; margin:0;}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin:0; padding:0;
}
</style>

