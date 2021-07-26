<template>
  <div class="login">
    <div class="heading">
      <h2>Sign in</h2>
      <form
        id="loginForm"
        @submit.prevent="submitForm"
      >
        <div class="input-group input-group-lg">
          <span class="input-group-addon"><i class="fa fa-user" /></span>
          <input
            v-model="username"
            type="text"
            class="form-control"
            placeholder="Username or email"
          >
        </div>

        <div class="input-group input-group-lg">
          <span class="input-group-addon"><i class="fa fa-lock" /></span>
          <input
            v-model="password"
            type="password"
            class="form-control"
            placeholder="Password"
          >
        </div>

        <button
          type="submit"
          class="float"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data: function() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    submitForm: function() {
      // event.preventDefault();
      console.log(this.username, this.password);
      var url = 'https://jsonplaceholder.typicode.com/users';
      var data = {
        username: this.username,
        password: this.password
      }
      axios.post(url, data)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
}
</script>


<style>


#loginForm input{
  border: black solid 1px;
}

.float{
  border: solid 1px;
  background:aqua;

}

</style>
