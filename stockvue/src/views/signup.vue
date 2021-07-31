<template>
  <div class="formContainer">
    <a class="blod">회원가입</a>
    <form class="login-box">
      <p>아이디</p>
      <input
        v-model="username"
        type="text"
        name="username"
        label="가입할 ID를 입력"
      >
      <p>이메일</p>
      <input
        v-model="email"
        type="text"
        name="email"
        label="가입할 이메일 입력"
      >
      <p>비밀번호</p>
      <input
        v-model="password1"
        type="password"
        name="userpassword1"
        label="비밀번호 입력"
      >
      <p>비밀번호 확인</p>
      <input
        v-model="password2"
        type="password"
        name="userpassword23"
        label="비밀번호 확인."
      >
      <br>
    </form>
    <div class="login-btn">
      <input
        type="submit"
        class="button"
        name="submit"
        value="회원가입"
        @click="signup({username, email, password1, password2})"
      >
    </div>
  </div>
</template>


<script>
import { mapState, mapActions} from "vuex";
export default {
  data(){
    return {
      username : null,
      email: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    ...mapActions(["signup"])
  },
};
</script>


<style>
input {
  border: black solid 1px;
}
.login-btn input{
  border-top: white solid 1px;
}

</style>
