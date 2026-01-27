<script setup>

import {useRoute} from "vue-router";

const route = useRoute();
</script>

<template>
person space: {{ route.params.user_id}}
</template>

<style scoped>

</style>