<template>
  <div class="formContainer">
    <form class="login-box">
      <p>아이디</p>
      <input
        v-model="username"
        type="text"
        name="username"
        label="ID를 입력하세요"
      >
      <!-- <p>이메일</p>
      <input
        v-model="email"
        type="text"
        name="email"
        label="email를 입력하세요"
      > -->
      <p>비밀번호</p>
      <input
        v-model="password"
        type="password"
        name="userpassword"
        label="비밀번호를 입력하세요"
      >
      <br>
    </form>
    <div class="login-btn">
      <input
        type="submit"
        class="button"
        name="submit"
        value="로그인"
        @click="login({username, password})"
      >
    </div>
  </div>
</template>
<script>
import { mapState, mapActions} from "vuex";

export default {
  components: {

  },
  data () {
    return {
      username : null,
      // email : null,
      password : null,

    };
  },
  computed: {
    ...mapState(["isLogin", "isLoginError"])
  },
  methods: {
    ...mapActions(["login"])
  }
};



// signup () {
//   // this.$refs.observer.validate()
//   this.$axios.post("http://127.0.0.1:8000/authUser/signup/", {
//     username :this.username,
//     password : this.password,
//     passwordConfirmation : this.passwordConfirmation
//   })
//     .then((res)=>{
//       console.log(res.data);
//       localStorage.setItem('jwt',res.data.token)
//       this.$router.push({ name : 'Login'})

//     })
// axios.post('http://127.0.0.1:8000/authUser/addresses/', {name = this.name,phone_number= this.phone_number,address = this.address })
// .then(res => console.log(res))

//   this.$axios.post("http://127.0.0.1:8000/authUser/addresses/",{
//     name = this.name,
//     phone_number= this.phone_number,
//     address = this.address
//   })
//     .then((res)=>{
//       alert("등록되길 바래");
//       console.log(res);
//     })
//     .then((err)=>{
//       console.log(err);
//     })

</script>
