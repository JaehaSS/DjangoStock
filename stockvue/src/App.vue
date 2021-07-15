<template>
  <div id="app">
    <Headerr />
    <div id="content" class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Headerr from './components/layout/Header.vue';



export default {
  name: 'App',
  components: {
    Headerr,
  }
}
</script>

<style>
</style>
