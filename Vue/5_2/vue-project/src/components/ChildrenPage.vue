<template>
  <div class="child" v-for="child in children.children">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
const children = defineProps({
                    children: Array,
                  })
console.log(children.children)
</script>

<style scoped>
.child {
  border: 1px solid rgb(190, 190, 190);
  padding: 10px;
  margin-top: 10px;
}
</style>