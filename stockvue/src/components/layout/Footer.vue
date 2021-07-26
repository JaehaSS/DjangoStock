<template>
  <v-footer

    padless
    class="justify-center"
  >
    <v-card
      flat
      tile
      class="indigo lighten-1 white--text text-center"
    >
      <v-card-text>
        <v-btn
          v-for="icon in icons"
          :key="icon.i"
          class="mx-4 white--text"
          icon
          @click="link1(icon.link)"
        >
          <v-icon
            size="24px"
          >
            {{ icon.i }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        안녕하세요. 궁금하신 점은 위 아이콘 클릭해서 문의 부탁드립니다. 감사합니다
      </v-card-text>

      <v-divider />

      <v-card-text class="white--text">
        <strong>Jaeha StockSite</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>
<script>
export default {
  name : "Footer",
  data () {
    return {


      icons: [
        {link: 'https:/www.facebook.com', i:'mdi-facebook'},
        {link: 'https://github.com/JaehaSS', i:'mdi-github'},
        {link: 'https:/www.google.com', i:'mdi-email'},
      ]

    }
  },methods:{
    link1:function(url){
      window.open(url);
    }
  }
}

</script>


<style scoped>
footer{border-top:1px solid #35495e; text-align:center; font-size:16px; color:#41b883; margin:100px 0 0 0;}
</style>
