import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Customers from '@/views/Customers.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/customers', component: Customers },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router