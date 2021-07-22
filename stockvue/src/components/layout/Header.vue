<template>
  <v-card>
    <v-tabs
      v-model="tab"
      background-color="deep-purple accent-4"
      centered
      icons-and-text
    >
      <v-tabs-slider />

      <v-tab href="/">
        Recents
        <v-icon>mdi-phone</v-icon>
      </v-tab>

      <v-tab href="/">
        Favorites
        <v-icon>mdi-heart</v-icon>
      </v-tab>

      <v-tab href="/about">
        Nearby
        <v-icon>mdi-account-box</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="i in 3"
        :key="i"
        :value="'tab-' + i"
      >
        <v-card flat>
          <v-card-text>{{ text }}</v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
export default {
  name : "Header",
  data () {
    return {
      tab: null,
      text: 'ㅁㄴㅇㅁㄴㅇ'
    }
  },
}
</script>

<style></style>
