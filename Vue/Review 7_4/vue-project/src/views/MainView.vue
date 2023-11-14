<template>
  <div>
    <h2>메인 페이지</h2>
    <hr>
    <MainPage
      v-for="balance in store.balances"
      :key="balance.name"
      :balance="balance"  
    />
  </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue'
import { useBalanceStore } from '@/stores/balance.js'

const store = useBalanceStore()
</script>

<style scoped>

</style>