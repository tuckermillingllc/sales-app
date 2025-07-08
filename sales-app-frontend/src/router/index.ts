import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Home,
      meta: { title: 'Tucker Milling Sales Dashboard' }
    },
    // Existing routes that work
    {
      path: '/customers',
      name: 'Customers',
      component: () => import('@/views/Customers.vue'),
      meta: { title: 'Customer Management' }
    },
    {
      path: '/about',
      name: 'About',
      component: () => import('@/views/AboutView.vue'),
      meta: { title: 'About Tucker Milling' }
    },
    // Placeholder routes (will be created later)
    {
      path: '/dealers',
      name: 'Dealers',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Active Dealers' }
    },
    {
      path: '/attention',
      name: 'Attention',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Attention Needed' }
    },
    {
      path: '/locator',
      name: 'DealerLocator',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Dealer Locator' }
    },
    {
      path: '/focus',
      name: 'FocusProducts',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Focus Products' }
    },
    {
      path: '/products',
      name: 'Products',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Product Catalog' }
    },
    {
      path: '/faq',
      name: 'FAQ',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Product FAQ' }
    },
    {
      path: '/comparison',
      name: 'Comparison',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Competitive Replacements' }
    },
    {
      path: '/selection',
      name: 'Selection',
      component: Home, // Temporarily redirect to home
      meta: { title: 'Product Selection Tool' }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Home, // Temporarily redirect to home
      meta: { title: 'User Profile' }
    }
  ]
})

// Update page title on route change
router.beforeEach((to) => {
  document.title = to.meta?.title as string || 'Tucker Milling Sales'
})

export default router