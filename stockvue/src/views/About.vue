<!-- fluid: 현재 화면 width 꽉 차게 함
  no-gutters : 요소 거리 삭제 기본 거터 사이즈 24픽셀



-->

<template>
  <h2>
    게시판리스트/h2>
    <btn @click="getList">
      Get방식데이터접근
    </btn>
  </h2>
</template>


<script>
export default {
  methods: {
    getList(){
      this.$axios.post("http://127.0.0.1:8000/authUser/addresses/")
        .then((res)=>{
          console.log(res);
        })
        .then((err)=>{
          console.log(err);
        })
    }
  }

};
</script>
