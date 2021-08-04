<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<template>
  <div>
    <v-btn
      text
      @click="pr"
    >
      <span>로그인하고 눌러보세요</span>
      <v-icon>mdi-power</v-icon>
    </v-btn>>
    <div v-if="isShow">
      <h1>{{ datalist.username }}님 안녕하세요</h1>
      <h1> 오늘의 주요 뉴스는 </h1>
      <ul>
        <li
          v-for="(i, j) in stockdatalist"
          :key="i"
        >
          <!-- <h3><a :href= i>{{j}}</a> </h3> -->
          <h3>
            <a
              :href="link(i)"
              target="_blank"
            >{{ j }}</a>
          </h3>
        </li>
      </ul>
    </div>
    <div v-else>
      <h1>안녕하세요</h1>
      <h1>로그인 부탁드립니다</h1>
    </div>
  </div>
</template>
<script>

export default {

  data (){
    return {

      stockdatalist : {},
      isShow : false,
      datalist : [],
      token :  'JWT ' + localStorage.getItem("access_token")
    }
  },
  methods: {
    pr () {
        this.$axios.get("http://localhost:8000/api/rest-auth/user/", {
        headers : this.listToken()
      })
        .then((res)=>{
          console.log(res.data);
          this.datalist = res.data
          this.isShow = true;
          this.stockdata();
        })
        .catch(() => {
          console.log(res.data)
        });
    },
    listToken (){
    const config = {
      Authorization : this.token
    }
    return config
  },
  stockdata() {
    this.$axios.get("http://localhost:8000/api/stockdata/?format=json",{
      headers : this.listToken()
    })
      .then(res => {
        console.log(res.data);
        this.stockdatalist = res.data
      })
  },
  link(data) {
    const ab = "https://finance.naver.com/" + data

    return ab

  }
 }
};
</script>
<style>
ul,li {
  list-style: none;
}
ul li a{
  text-decoration: none;
}
ul li:hover{
  display: inline-block;
  background-color:cornflowerblue

}



</style>



