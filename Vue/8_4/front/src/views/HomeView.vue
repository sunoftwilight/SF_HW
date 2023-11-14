<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <button @click="goCreate">게시글 생성</button>
    <ArticleList
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import { onMounted } from 'vue'

const router = useRouter()
const store = useArticleStore()

const goCreate = function () {
  router.push({ name: 'create' })
}

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>