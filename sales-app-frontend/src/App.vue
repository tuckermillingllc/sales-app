<template>
  <div id="app">
    <!-- Main Content Area -->
    <main class="main-content">
      <RouterView />
    </main>

    <!-- Bottom Navigation -->
    <BottomNavigation 
      :current-tab="currentTab" 
      :alert-count="5"
      @tab-change="handleTabChange" 
    />
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import BottomNavigation from '@/components/BottomNavigation.vue'

const route = useRoute()
const router = useRouter()

// Current tab state
const currentTab = ref('dashboard')

// Watch route changes to update current tab
watch(
  () => route.path,
  (newPath) => {
    // Map routes to tab names
    const routeToTab: Record<string, string> = {
      '/': 'dashboard',
      '/dealers': 'dealers',
      '/products': 'products',
      '/locator': 'map',
      '/attention': 'alerts',
      '/profile': 'profile'
    }
    
    currentTab.value = routeToTab[newPath] || 'dashboard'
  },
  { immediate: true }
)

// Handle tab changes from bottom navigation
const handleTabChange = (tab: string) => {
  currentTab.value = tab
  
  // Navigate based on tab
  const tabToRoute: Record<string, string> = {
    'dashboard': '/',
    'dealers': '/dealers',
    'products': '/products',
    'map': '/locator',
    'alerts': '/attention',
    'profile': '/profile'
  }
  
  const targetRoute = tabToRoute[tab]
  if (targetRoute && targetRoute !== route.path) {
    router.push(targetRoute)
  }
}
</script>

<style>
/* Global App Styles */
#app {
  font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
  background: linear-gradient(180deg, var(--bg-light, #f8fafc) 0%, #e2e8f0 100%);
  min-height: 100vh;
  color: var(--text-dark, #1a202c);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Fix status bar background to match page */
body {
  background: #fafbfc !important;
  margin: 0;
  padding: 0;
}

/* Ensure the viewport background matches */
html {
  background: #fafbfc !important;
}

/* Status bar area styling for iOS */
@supports (padding-top: env(safe-area-inset-top)) {
  body {
    padding-top: env(safe-area-inset-top);
    background: #fafbfc !important;
  }
}

.main-content {
  padding-bottom: 80px; /* Space for bottom navigation */
  min-height: calc(100vh - 80px);
  background: #fafbfc;
}

/* Ensure RouterView transitions work smoothly */
.router-view {
  transition: all 0.3s ease;
}

/* Global responsive adjustments */
@media (max-width: 768px) {
  .main-content {
    padding-bottom: 70px;
  }
}
</style>