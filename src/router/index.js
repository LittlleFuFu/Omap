// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/VotesPage.vue'
import PartyPage from '../views/PartyPage.vue'

const routes = [
  {
    path: '/',
    name: 'VotesPage',
    component: HomePage
  },
  {
    path: '/PartyPage',
    name: 'PartyPage',
    component: PartyPage
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
