<template>
  <div class="bottom-nav">
    <div class="nav-container">
      <a 
        v-for="item in navItems" 
        :key="item.id"
        href="#" 
        class="nav-item" 
        :class="{ active: currentTab === item.id }"
        @click.prevent="handleTabClick(item.id)"
      >
        <div class="nav-icon">
          <svg v-if="item.id === 'dashboard'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
            <polyline points="9,22 9,12 15,12 15,22"/>
          </svg>
          <svg v-else-if="item.id === 'dealers'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/>
            <path d="M6 12h4v4H6z"/>
            <path d="M14 12h4v4h-4z"/>
            <path d="M6 20h4v2H6z"/>
            <path d="M14 20h4v2h-4z"/>
            <path d="M6 4h4v4H6z"/>
            <path d="M14 4h4v4h-4z"/>
          </svg>
          <svg v-else-if="item.id === 'products'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 8a2 2 0 0 0-1-1.73L12 2 4 6.27A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73L12 22l8-4.27A2 2 0 0 0 21 16Z"/>
            <path d="M3.29 7 12 12l8.71-5"/>
            <path d="M12 22V12"/>
          </svg>
          <svg v-else-if="item.id === 'map'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
          <svg v-else-if="item.id === 'alerts'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
            <path d="M12 9v4"/>
            <path d="M12 17h.01"/>
          </svg>
        </div>
        <div class="nav-label">{{ item.label }}</div>
        <div 
          v-if="item.id === 'alerts' && alertCount > 0" 
          class="nav-badge"
        >
          {{ alertCount }}
        </div>
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
interface NavItem {
  id: string
  label: string
}

defineProps<{
  currentTab: string
  alertCount: number
}>()

const emit = defineEmits<{
  tabChange: [tab: string]
}>()

const navItems: NavItem[] = [
  { id: 'dashboard', label: 'DASHBOARD' },
  { id: 'dealers', label: 'DEALERS' },
  { id: 'products', label: 'PRODUCTS' },
  { id: 'map', label: 'MAP' },
  { id: 'alerts', label: 'ALERTS' }
]

const handleTabClick = (tab: string) => {
  // Haptic feedback simulation
  if (navigator.vibrate) {
    navigator.vibrate(5)
  }
  
  emit('tabChange', tab)
}
</script>

<style scoped>
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #ffffff;
  border-top: 1px solid #e5e7eb;
  padding: 8px 0 max(8px, env(safe-area-inset-bottom));
  z-index: 1000;
  box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.05);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0 16px;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px 12px;
  text-decoration: none;
  color: #9ca3af;
  transition: all 0.2s ease;
  border-radius: 8px;
  min-width: 60px;
  position: relative;
}

.nav-item:hover,
.nav-item.active {
  color: #1f2937;
}

.nav-item.active {
  background: #f9fafb;
}

.nav-icon {
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-icon svg {
  width: 20px;
  height: 20px;
  stroke-width: 1.5;
}

.nav-label {
  font-size: 0.625rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1;
  color: inherit;
}

.nav-badge {
  position: absolute;
  top: 2px;
  right: 6px;
  background: #ef4444;
  color: white;
  border-radius: 10px;
  padding: 2px 6px;
  font-size: 0.625rem;
  font-weight: 700;
  min-width: 18px;
  text-align: center;
  line-height: 1.2;
  box-shadow: 0 1px 3px rgba(239, 68, 68, 0.3);
}

@media (max-width: 768px) {
  .nav-container {
    padding: 0 8px;
  }

  .nav-item {
    padding: 6px 8px;
    min-width: 52px;
  }

  .nav-icon svg {
    width: 18px;
    height: 18px;
  }

  .nav-label {
    font-size: 0.5rem;
  }
}
</style>