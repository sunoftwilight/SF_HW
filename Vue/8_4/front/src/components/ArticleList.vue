<template>
  <div>
    <h5>{{ article.id }}번 게시글</h5>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()

defineProps({
  article: Object,
})

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

</style>