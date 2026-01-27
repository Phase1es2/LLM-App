<script setup>
import {ref} from "vue";
import {useUserStore} from "@/stores/user.js";
import {useRouter} from "vue-router";
import api from "@/js/http/api.js";

const username = ref('')
const password = ref('')
const errorMessage = ref('')

const user = useUserStore()
const router = useRouter()

async function handleLogin() {
  errorMessage.value = ''
  if (!username.value.trim()) {
    errorMessage.value = 'username is required'
  } else if (!password.value.trim()) {
    errorMessage.value = 'password is required'
  } else {
    try {
      const res = await api.post('/api/user/account/login/', {
        username: username.value,
        password: password.value,
      })
      const data = res.data
      if (data.result === 'success') {
        user.setAccessToken(data.access)
        user.setUserInfo(data)
        await router.push({
          name: 'homepage-index'
        })
      } else {
        errorMessage.value = data.result
      }
    } catch (err) {
    }
  }
}
</script>


<template>
  <div class="flex justify-center mt-30">
    <form @submit.prevent="handleLogin" class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <label class="label">Username</label>
      <input v-model="username" type="text" class="input" placeholder="Username" />

      <label class="label">Password</label>
      <input v-model="password" type="password" class="input" placeholder="Password" />

      <p v-if="errorMessage" class="text-sm text-red-500 mt-1">{{ errorMessage }}</p>

      <button class="btn btn-neutral mt-4">Login</button>
      <div class="flex justify-end">
        <RouterLink :to="{name: 'register-index'}" class="btn btn-sm btn-ghost text-gray-500">
          Register
        </RouterLink>
      </div>
    </form>
  </div>

</template>

<style scoped>

</style>