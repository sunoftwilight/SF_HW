<template>
  <div class="parent">
    <h1>부모 페이지입니다.</h1>
    <ChildrenPage :children="children" />
  </div>
</template>

<script setup>
import ChildrenPage from '@/components/ChildrenPage.vue'
import { ref } from 'vue'

const children = ref([
  {name: '김하나', age: 30},
  {name: '김두리', age: 20},
  {name: '김서이', age: 10},
])
</script>

<style scoped>
.parent {
  border: 1px solid rgb(190, 190, 190);
  padding: 10px;
}
</style>