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
        href="/signup"
        target="_self"
        text
      >
        <span class="mr-2">회원 가입</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Application
          </v-list-item-title>
          <v-list-item-subtitle>
            subtext
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
  </v-app>
</template>
<script>
// import Header from './components/layout/Header'
// import Footer from './components/layout/Footer.vue'
// import Content from '/components/layout/Content.vue'
export default {
  name: 'App',

  components: {
    // Header, Footer, Content
  },

  data: ()=> ({
    drawer:false,
    items: [
      { title: 'Home', icon: 'mdi-view-dashboard', to:'/' },
      { title: 'Photos', icon: 'mdi-image', to :'/about' },
      { title: 'About', icon: 'mdi-help-box', to :'/signup' },
    ],
    right: null,
  }),

};
</script>
