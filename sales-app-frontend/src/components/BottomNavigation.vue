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
        <div class="nav-icon">{{ item.icon }}</div>
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
  icon: string
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
  { id: 'dashboard', icon: '🏠', label: 'Dashboard' },
  { id: 'dealers', icon: '🏪', label: 'Dealers' },
  { id: 'products', icon: '🌾', label: 'Products' },
  { id: 'map', icon: '📍', label: 'Map' },
  { id: 'alerts', icon: '⚠️', label: 'Alerts' },
  { id: 'profile', icon: '👤', label: 'Profile' }
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
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-top: 1px solid rgba(226, 232, 240, 0.8);
  padding: 8px 0 16px 0;
  z-index: 1000;
  box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.06);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 0 24px;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px 12px;
  text-decoration: none;
  color: var(--text-light);
  transition: all 0.2s ease;
  border-radius: 12px;
  min-width: 64px;
  position: relative;
}

.nav-item:hover,
.nav-item.active {
  color: var(--primary-blue);
  background: rgba(30, 58, 138, 0.1);
}

.nav-icon {
  font-size: 20px;
  margin-bottom: 4px;
}

.nav-label {
  font-size: 0.7rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.nav-badge {
  position: absolute;
  top: 4px;
  right: 8px;
  background: var(--primary-red);
  color: white;
  border-radius: 8px;
  padding: 2px 6px;
  font-size: 0.6rem;
  font-weight: 600;
  min-width: 16px;
  text-align: center;
}

@media (max-width: 768px) {
  .nav-container {
    padding: 0 16px;
  }

  .nav-item {
    padding: 6px 8px;
    min-width: 56px;
  }

  .nav-icon {
    font-size: 18px;
  }

  .nav-label {
    font-size: 0.6rem;
  }
}
</style>