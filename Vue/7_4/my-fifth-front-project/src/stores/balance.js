import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    },
  ])

  const addBalance = function (userName) {
    const user = balances.value.filter((balance) => balance.name === userName)[0]
    user.balance += 1000
  }

  const balanceResult = computed(() => {
    return (userInfo) => balances.value.find((balance) => balance.name === userInfo).balance
  })

  return { balances, addBalance, balanceResult }
})
