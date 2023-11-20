import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  const token = ref(null)
  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function ({ username, password1, password2 }) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username, password1, password2
      },
    })
      .then((res) => {
        token.value = res.data.key
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function ({ username, password }) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
  }

  return { articles, getArticles, createArticle, signUp, logIn, token }
})
