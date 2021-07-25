<template>
  <validation-observer
    ref="observer"
    v-slot="{ invalid }"
  >
    <form @submit.prevent="submit">
      <validation-provider
        v-slot="{ errors }"
        name="Name"
        rules="required|max:10"
      >
        <v-text-field
          ref="name"
          v-model="name"
          :counter="10"
          :error-messages="errors"
          label="이름"
          required
        />
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="올바르지 않습니다"
        :rules="{
          required: true,
          digits: 11,
          regex: '^[0-9]'
        }"
      >
        <v-text-field
          ref="phone_number"
          v-model="phone_number"
          :counter="12"
          :error-messages="errors"
          label="핸드폰 번호(-뺴고 기입해주세요)"
          required
        />
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="address"
        rules="required|max:20"
      >
        <v-text-field
          ref="address"
          v-model="address"
          :counter="20"
          :error-messages="errors"
          label="주소"
          required
        />
      </validation-provider>
      <!-- <validation-provider
        v-slot="{ errors }"
        name="email"
        rules="required|email"
      >
        <v-text-field
          v-model="email"
          :error-messages="errors"
          label="이메일"
          required
        />
      </validation-provider> -->
      <validation-provider
        v-slot="{ errors }"
        rules="required"
        name="checkbox"
      >
        <v-checkbox
          v-model="checkbox"
          :error-messages="errors"
          value="1"
          label="개인 정보 동의"
          type="checkbox"
          required
        />
      </validation-provider>

      <v-btn
        class="mr-4"
        type="submit"
        :disabled="invalid"
      >
        확인
      </v-btn>
      <v-btn @click="clear">
        새로고침
      </v-btn>
    </form>
  </validation-observer>
</template>

<script>
import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

setInteractionMode('eager')

extend('digits', {
  ...digits,
  message: '{_field_}  ({_value_})',
})

extend('required', {
  ...required,
  message: '개인 정보 동의 체크해주세요',
})

extend('max', {
  ...max,
  message: '{_field_} may not be greater than {length} characters',
})

extend('regex', {
  ...regex,
  message: '{_field_} {_value_} does not match {regex}',
})

// extend('email', {
//   ...email,
//   message: 'Email must be valid',
// })

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    name: '',
    phone_number: '',
    address: '',
    select: null,
    checkbox: null,
  }),

  methods: {
    submit () {
      // this.$refs.observer.validate()
      this.$axios.post("http://127.0.0.1:8000/authUser/addresses/", {
        name :this.name,
        phone_number:this.phone_number,
        address:this.address})
        .then((res)=>{
          alert("등록되길 바래");
          console.log(res.data);
        })
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
    },
    clear () {
      this.name = ''
      this.phoneNumber = ''
      this.email = ''
      this.select = null
      this.checkbox = null
      this.$refs.observer.reset()
    },
  },
}
</script>
