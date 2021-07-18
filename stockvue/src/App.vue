<template>
  <div id="app">
    <Header />
    <div id="content" class="content">
      <router-view></router-view>
    </div>
    <Footer />
  </div>
  
</template>

<script>
import Footer from './components/layout/Footer.vue';
import Header from './components/layout/Header.vue';



export default {
  name: 'App',
  components: {
    Header,
    Footer,
  }
}
</script>

<style>
</style>
