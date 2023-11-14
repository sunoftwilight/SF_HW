<template>
  <nav>
    <RouterLink :to="{ name: 'main' }">main</RouterLink>
  </nav>
  <h1>pinia + router 연습하기</h1>
  <RouterLink :to="{ name: 'main' }"></RouterLink>
  <!-- <RouterLink :to="{ name: 'update', params: {name: } }"></RouterLink> -->
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
