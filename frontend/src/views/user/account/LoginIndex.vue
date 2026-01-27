<script setup>

</script>

<template>
  <div class="flex justify-center mt-30">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">

      <label class="label">Username</label>
      <input type="text" class="input" placeholder="Username" />

      <label class="label">Password</label>
      <input type="password" class="input" placeholder="Password" />

      <button class="btn btn-neutral mt-4">Login</button>
      <div class="flex justify-end">
        <RouterLink :to="{name: 'register-index'}" class="btn btn-sm btn-ghost text-gray-50">Register</RouterLink>
      </div>
    </fieldset>
  </div>
</template>

<style scoped>

</style>