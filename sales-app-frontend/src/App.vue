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
  background: #ffffff;
  min-height: 100vh;
  color: var(--text-dark, #1a202c);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* Add padding for safe areas */
  padding-top: env(safe-area-inset-top);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* Fix status bar background to match page */
body {
  background: #ffffff !important; /* CHANGED: Was #fafbfc, now white */
  margin: 0;
  padding: 0;
}

/* Ensure the viewport background matches */
html {
  background: #ffffff !important; /* CHANGED: Was #fafbfc, now white */
}

/* Status bar area styling for iOS */

  body {
    padding-top: env(safe-area-inset-top);
    background: #ffffff !important; /* CHANGED: Was #fafbfc, now white */
  }


.main-content {
  padding-bottom: calc(80px + env(safe-area-inset-bottom)); /* Add safe area to bottom nav space */
  min-height: calc(100vh - env(safe-area-inset-top) - 80px - env(safe-area-inset-bottom));
  background: #ffffff;
}

/* Ensure RouterView transitions work smoothly */
.router-view {
  transition: all 0.3s ease;
}

/* Global responsive adjustments */
@media (max-width: 768px) {
  .main-content {
    padding-bottom: calc(70px + env(safe-area-inset-bottom));
  }
}
</style>