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
    {
      path: '/dealers',
      name: 'Dealers',
      component: () => import('@/views/DealersView.vue'),
      meta: { title: 'Active Dealers' }
    },
    {
      path: '/attention',
      name: 'Attention',
      component: () => import('@/views/AttentionView.vue'),
      meta: { title: 'Attention Needed' }
    },
    {
      path: '/locator',
      name: 'DealerLocator',
      component: () => import('@/views/LocatorView.vue'),
      meta: { title: 'Dealer Locator' }
    },
    {
      path: '/focus',
      name: 'FocusProducts',
      component: () => import('@/views/FocusView.vue'),
      meta: { title: 'Focus Products' }
    },
    {
      path: '/products',
      name: 'Products',
      component: () => import('@/views/ProductsView.vue'),
      meta: { title: 'Product Catalog' }
    },
    {
      path: '/faq',
      name: 'FAQ',
      component: () => import('@/views/FAQView.vue'),
      meta: { title: 'Product FAQ' }
    },
    {
      path: '/comparison',
      name: 'Comparison',
      component: () => import('@/views/ComparisonView.vue'),
      meta: { title: 'Competitive Replacements' }
    },
    {
      path: '/selection',
      name: 'Selection',
      component: () => import('@/views/SelectionView.vue'),
      meta: { title: 'Product Selection Tool' }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: () => import('@/views/ProfileView.vue'),
      meta: { title: 'User Profile' }
    },
    // Legacy routes
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
    }
  ]
})

// Update page title on route change
router.beforeEach((to) => {
  document.title = to.meta?.title as string || 'Tucker Milling Sales'
})

export default router