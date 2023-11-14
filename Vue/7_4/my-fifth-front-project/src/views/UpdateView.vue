<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ userInfo }}</p>
    <p>잔고 : {{ store.balanceResult(userInfo) }}</p>
    <button @click="store.addBalance(userInfo)">+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const userInfo = ref(route.params.name)
const store = useBalanceStore()
</script>

<style scoped>

</style>