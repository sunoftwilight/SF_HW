<template>
  <div>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="goUpdate(balance.name)">updateBalance</button>
  </div>
</template>

<script setup>
import router from '../router';

defineProps({
  balance: Object,
})

const goUpdate = function (balanceName) {
  router.push({ name: 'update', params: { name: balanceName }})
}
</script>

<style scoped>

</style>