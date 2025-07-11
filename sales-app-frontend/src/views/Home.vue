<template>
  <f7-page ptr @ptr:refresh="onRefresh">
    <div class="dashboard">
      <!-- Header Section -->
      <div class="header">
    <div class="header-content">
      <div class="brand-section">
        <div class="logo-container">
          <img :src="tuckerLogo" alt="Tucker Milling" class="company-logo" />
        </div>
        <div class="brand-text">
          <p class="welcome-message">Welcome Curran!</p>
          <p class="tagline">Sales Management Portal</p>
        </div>
      </div>
    <div class="stats-overview-grid">
    <div class="stat-item">
      <span class="stat-value">{{ totalDealers }}</span>
      <span class="stat-label">Active Dealers</span>
    </div>
    <div class="stat-item">
      <span class="stat-value">{{ attentionCount }}</span>
      <span class="stat-label">Need Attention</span>
    </div>
    <div class="stat-item products-stat">
      <span class="stat-value">156</span>
      <span class="stat-label">Products</span>
    </div>
  </div>
  </div>
      </div>

      <!-- Main Dashboard Grid -->
      <div class="dashboard-grid">
        <!-- Active Dealers Card -->
        <div class="dashboard-card primary-card" @click="navigateTo('/dealers')">
          <div class="card-header">
            <div class="card-icon dealers-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-4m-5 0H3m2 0v-3.5a3.5 3.5 0 013.5-3.5h.75"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Active Dealers</h3>
              <p class="card-subtitle">Performance tracking</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="metrics-row">
              <div class="metric">
                <span class="metric-value positive">+12.5%</span>
                <span class="metric-label">Monthly Growth</span>
              </div>
              <div class="metric">
                <span class="metric-value">{{ activeDealers.length }}</span>
                <span class="metric-label">Top Performers</span>
              </div>
            </div>
            <div class="preview-list">
              <div v-for="dealer in activeDealers.slice(0, 3)" :key="dealer.id" class="list-item">
                <div class="item-content">
                  <span class="item-name">{{ dealer.name }}</span>
                  <span class="item-location">{{ getLocation(dealer.name) }}</span>
                </div>
                <span class="item-metric positive">{{ dealer.metric }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Attention Required Card -->
        <div class="dashboard-card warning-card" @click="navigateTo('/attention')">
          <div class="card-header">
            <div class="card-icon attention-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
                <path d="M12 9v4m0 4h.01"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Attention Required</h3>
              <p class="card-subtitle">Dealer support needed</p>
            </div>
            <div class="notification-badge">{{ attentionCount }}</div>
          </div>
          <div class="card-content">
            <div class="alert-summary">
              <div class="alert-item urgent">
                <span class="alert-count">2</span>
                <span class="alert-label">Critical Issues</span>
              </div>
              <div class="alert-item moderate">
                <span class="alert-count">3</span>
                <span class="alert-label">Declining Sales</span>
              </div>
            </div>
            <div class="preview-list">
              <div v-for="dealer in attentionDealers.slice(0, 3)" :key="dealer.id" class="list-item">
                <div class="item-content">
                  <span class="item-name">{{ dealer.name }}</span>
                  <span class="item-status" :class="dealer.status">{{ getStatusText(dealer.status) }}</span>
                </div>
                <span class="item-metric" :class="dealer.metricType">{{ dealer.metric }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Dealer Network Card -->
        <div class="dashboard-card secondary-card" @click="navigateTo('/locator')">
          <div class="card-header">
            <div class="card-icon location-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Dealer Network</h3>
              <p class="card-subtitle">Location & coverage</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="network-stats">
              <div class="coverage-item">
                <span class="coverage-value">85%</span>
                <span class="coverage-label">Territory Coverage</span>
              </div>
              <div class="coverage-item">
                <span class="coverage-value">12</span>
                <span class="coverage-label">States Active</span>
              </div>
            </div>
            <div class="location-list">
              <div v-for="location in nearbyDealers.slice(0, 3)" :key="location.id" class="location-item">
                <div class="location-info">
                  <span class="location-name">{{ location.name }}</span>
                  <span class="location-address">{{ location.address }}</span>
                </div>
                <span class="distance-badge">{{ location.distance }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Product Management Card -->
        <div class="dashboard-card secondary-card" @click="navigateTo('/products')">
          <div class="card-header">
            <div class="card-icon products-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 8a2 2 0 0 0-1-1.73L12 2 4 6.27A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73L12 22l8-4.27A2 2 0 0 0 21 16Z"/>
                <path d="M3.29 7 12 12l8.71-5"/>
                <path d="M12 22V12"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Product Catalog</h3>
              <p class="card-subtitle">Feed & nutrition</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="product-categories">
              <div v-for="category in productCategories.slice(0, 4)" :key="category.id" class="category-pill">
                {{ category.name }}
              </div>
            </div>
            <div class="product-stats">
              <div class="product-metric">
                <span class="metric-value">156</span>
                <span class="metric-label">Active Products</span>
              </div>
              <div class="product-metric">
                <span class="metric-value">6</span>
                <span class="metric-label">Categories</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Priority Products Card -->
        <div class="dashboard-card accent-card" @click="navigateTo('/focus')">
          <div class="card-header">
            <div class="card-icon focus-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <circle cx="12" cy="12" r="6"/>
                <circle cx="12" cy="12" r="2"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Priority Products</h3>
              <p class="card-subtitle">Focus initiatives</p>
            </div>
            <div class="priority-indicator high">HIGH</div>
          </div>
          <div class="card-content">
            <div class="priority-list">
              <div v-for="product in focusProducts" :key="product.id" class="priority-item">
                <div class="priority-content">
                  <span class="product-name">{{ product.name }}</span>
                  <span class="priority-reason">{{ getProductReason(product.name) }}</span>
                </div>
                <div class="priority-badge" :class="product.priority">
                  {{ product.priority?.toUpperCase() }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Knowledge Base Card -->
        <div class="dashboard-card secondary-card" @click="navigateTo('/faq')">
          <div class="card-header">
            <div class="card-icon knowledge-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                <path d="M12 17h.01"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Frequently Asked Questions</h3>
              <p class="card-subtitle">Product information</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="knowledge-stats">
              <div class="knowledge-metric">
                <span class="metric-value">{{ frequentQuestions.length }}+</span>
                <span class="metric-label">FAQs Available</span>
              </div>
              <div class="knowledge-metric">
                <span class="metric-value">98%</span>
                <span class="metric-label">Query Resolution</span>
              </div>
            </div>
            <div class="recent-queries">
              <div v-for="question in frequentQuestions.slice(0, 2)" :key="question.id" class="query-item">
                {{ question.question }}
              </div>
            </div>
          </div>
        </div>

        <!-- Competitive Analysis Card -->
        <div class="dashboard-card secondary-card" @click="navigateTo('/comparison')">
          <div class="card-header">
            <div class="card-icon competitive-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M8 3v3a2 2 0 0 1-2 2H3"/>
                <path d="M21 8h-3a2 2 0 0 1-2-2V3"/>
                <path d="M3 16h3a2 2 0 0 1 2 2v3"/>
                <path d="M16 21v-3a2 2 0 0 1 2-2h3"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Competitive Analysis</h3>
              <p class="card-subtitle">Market positioning</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="competitive-overview">
              <div class="competitive-metric">
                <span class="metric-value">{{ competitiveReplacements.length }}</span>
                <span class="metric-label">Replacements</span>
              </div>
              <div class="competitive-metric">
                <span class="metric-value">25%</span>
                <span class="metric-label">Avg. Savings</span>
              </div>
            </div>
            <div class="replacement-preview">
              <div class="replacement-item">
                <span class="competitor-name">Leading Competitor</span>
                <span class="replacement-arrow">→</span>
                <span class="tucker-solution">Tucker Alternative</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Selection Tool Card -->
        <div class="dashboard-card tertiary-card" @click="navigateTo('/selection')">
          <div class="card-header">
            <div class="card-icon selection-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 11H3l5-5m0 0v14l-5-5"/>
                <path d="M21 3l-9 9-3-3"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Product Selection</h3>
              <p class="card-subtitle">Recommendation engine</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="selection-process">
              <div class="process-step">
                <div class="step-indicator">1</div>
                <span class="step-label">Animal Requirements</span>
              </div>
              <div class="process-step">
                <div class="step-indicator">2</div>
                <span class="step-label">Nutritional Analysis</span>
              </div>
              <div class="process-step">
                <div class="step-indicator">3</div>
                <span class="step-label">Product Matching</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Top 20 Products Card -->
        <div class="dashboard-card secondary-card" @click="navigateTo('/top-products')">
          <div class="card-header">
            <div class="card-icon top-products-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>
                <rect x="8" y="2" width="8" height="4" rx="1" ry="1"/>
                <path d="M12 11h4"/>
                <path d="M12 16h4"/>
                <path d="M8 11h.01"/>
                <path d="M8 16h.01"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Top Products</h3>
              <p class="card-subtitle">Best sellers this month</p>
            </div>
            <div class="card-action">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="ranking-stats">
              <div class="ranking-metric">
                <span class="metric-value">20</span>
                <span class="metric-label">Products Ranked</span>
              </div>
              <div class="ranking-metric">
                <span class="metric-value">$485K</span>
                <span class="metric-label">Total Revenue</span>
              </div>
            </div>
            <div class="top-products-list">
              <div v-for="(product, index) in topProducts" :key="product.id" class="ranking-item">
                <div class="rank-indicator">{{ index + 1 }}</div>
                <div class="product-details">
                  <span class="product-name">{{ product.name }}</span>
                  <span class="product-category">{{ product.category }}</span>
                </div>
                <div class="sales-data">
                  <span class="sales-volume">{{ product.salesVolume }}</span>
                  <span class="revenue-amount">${{ product.revenue }}K</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Fastest Growing Products Card -->
        <div class="dashboard-card accent-card" @click="navigateTo('/growing-products')">
          <div class="card-header">
            <div class="card-icon growth-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 3v18h18"/>
                <path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"/>
                <path d="M13 7h6v6"/>
              </svg>
            </div>
            <div class="card-title-section">
              <h3 class="card-title">Fastest Growing</h3>
              <p class="card-subtitle">Trending products</p>
            </div>
            <div class="trending-indicator">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M7 17l9.2-9.2M17 17V7H7"/>
              </svg>
            </div>
          </div>
          <div class="card-content">
            <div class="growth-summary">
              <div class="growth-metric">
                <span class="metric-value growth-positive">+28%</span>
                <span class="metric-label">Avg Growth Rate</span>
              </div>
              <div class="growth-metric">
                <span class="metric-value">5</span>
                <span class="metric-label">Trending Products</span>
              </div>
            </div>
            <div class="growth-products-list">
              <div v-for="product in fastestGrowingProducts" :key="product.id" class="growth-item">
                <div class="product-info">
                  <span class="product-name">{{ product.name }}</span>
                  <span class="growth-period">{{ product.period }}</span>
                </div>
                <div class="growth-indicator-badge" :class="getGrowthClass(product.growthRate)">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M7 17l9.2-9.2M17 17V7H7"/>
                  </svg>
                  {{ product.growthRate }}%
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </f7-page>
</template>

<script setup lang="ts">
import { ref, computed, onMounted} from 'vue'
import { useRouter } from 'vue-router'
import tuckerLogo from '@/assets/tucker-logo.png'
import '@/styles/dashboard.css'

// Types
interface Dealer {
  id: number
  name: string
  status: 'active' | 'declining' | 'stopped'
  metric: string
  metricType: 'positive' | 'negative' | 'warning'
}

interface Product {
  id: number
  name: string
  priority?: 'high' | 'medium'
  category?: string
}

interface Question {
  id: number
  question: string
}

interface Location {
  id: number
  name: string
  address: string
  distance: string
}

interface Replacement {
  id: number
  competitor: string
  competitorProduct: string
  tuckerProduct: string
}

interface TopProduct {
  id: number
  name: string
  category: string
  salesVolume: string
  revenue: number
}

interface GrowingProduct {
  id: number
  name: string
  period: string
  growthRate: number
}

// Router
const router = useRouter()

// Reactive data
const totalDealers = ref(0)

// Sample data
const activeDealers = ref<Dealer[]>([])

const attentionDealers = ref<Dealer[]>([])

const nearbyDealers = ref<Location[]>([
  { id: 1, name: 'Southern States Co-op', address: 'Huntsville, AL', distance: '12 mi' },
  { id: 2, name: 'Farmers Feed & Seed', address: 'Scottsboro, AL', distance: '18 mi' },
  { id: 3, name: 'Country Boy Feed Store', address: 'Arab, AL', distance: '22 mi' }
])

const focusProducts = ref<Product[]>([
  { id: 1, name: 'Show Flock Layer 22', priority: 'high' },
  { id: 2, name: 'Strategy Healthy Edge', priority: 'high' },
  { id: 3, name: 'Safe Choice Horse Feed', priority: 'medium' },
  { id: 4, name: 'Ultium Growth', priority: 'medium' }
])

const productCategories = ref<Product[]>([
  { id: 1, name: 'Horse Feed' },
  { id: 2, name: 'Cattle Feed' },
  { id: 3, name: 'Poultry Feed' },
  { id: 4, name: 'Swine Feed' },
  { id: 5, name: 'Sheep Feed' },
  { id: 6, name: 'Supplements' }
])

const frequentQuestions = ref<Question[]>([
  { id: 1, question: 'Niacin content in Show Flock Layer 22?' },
  { id: 2, question: 'Lowest NSC horse feed available?' },
  { id: 3, question: 'Best feed for HYPP horses?' },
  { id: 4, question: 'Protein content in Ultium Competition?' }
])

const competitiveReplacements = ref<Replacement[]>([
  { id: 1, competitor: 'Purina', competitorProduct: 'Strategy Healthy Edge', tuckerProduct: 'Easy Keeper 12' },
  { id: 2, competitor: 'Nutrena', competitorProduct: 'SafeChoice Senior', tuckerProduct: 'Senior Complete' },
  { id: 3, competitor: 'Triple Crown', competitorProduct: 'Senior Formula', tuckerProduct: 'Golden Years' }
])

const topProducts = ref<TopProduct[]>([
  { id: 1, name: 'Show Flock Layer 22', category: 'Poultry Feed', salesVolume: '2,450 bags', revenue: 98 },
  { id: 2, name: 'Strategy Healthy Edge', category: 'Horse Feed', salesVolume: '1,890 bags', revenue: 85 },
  { id: 3, name: 'Ultium Competition', category: 'Horse Feed', salesVolume: '1,675 bags', revenue: 78 },
  { id: 4, name: 'Safe Choice Original', category: 'Horse Feed', salesVolume: '1,540 bags', revenue: 72 },
  { id: 5, name: 'Broiler Maker 22', category: 'Poultry Feed', salesVolume: '1,320 bags', revenue: 65 }
])

const fastestGrowingProducts = ref<GrowingProduct[]>([
  { id: 1, name: 'Strategy Healthy Edge', period: 'Last 30 days', growthRate: 42 },
  { id: 2, name: 'Ultium Growth', period: 'Last 30 days', growthRate: 38 },
  { id: 3, name: 'Show Flock Layer 22', period: 'Last 30 days', growthRate: 28 },
  { id: 4, name: 'Broiler Maker 22', period: 'Last 30 days', growthRate: 24 },
  { id: 5, name: 'Safe Choice Senior', period: 'Last 30 days', growthRate: 18 }
])

onMounted(async () => {
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/api/v1/dashboard/stats`);
    const data = await res.json();
    console.log('Dashboard data:', data);

    // Validate before assigning
    if (data && Array.isArray(data.active_dealers) && Array.isArray(data.attention_dealers)) {
      totalDealers.value = data.active_count ?? 0;
      activeDealers.value = data.active_dealers;
      attentionDealers.value = data.attention_dealers;
    } else {
      console.error('Unexpected data structure:', data);
    }
  } catch (err) {
    console.error('Failed to fetch dashboard stats:', err);
  }
});

const getGrowthClass = (growthRate: number): string => {
  if (growthRate >= 35) return 'growth-high'
  if (growthRate >= 20) return 'growth-medium'
  return 'growth-low'
}

// Computed
const attentionCount = computed(() => attentionDealers.value.length)

// Methods
const navigateTo = (path: string) => {
  router.push(path)
}

const getLocation = (dealerName: string): string => {
  const locations: Record<string, string> = {
    'Farmland Feed & Supply': 'Huntsville, AL',
    'Heritage Farm Supply': 'Decatur, AL',
    'Country Store Co-op': 'Athens, AL',
    'Rural Feed Solutions': 'Madison, AL'
  }
  return locations[dealerName] || 'Alabama'
}

const getStatusText = (status: string): string => {
  const statusMap: Record<string, string> = {
    'declining': 'Declining Sales',
    'stopped': 'No Recent Orders',
    'active': 'Active'
  }
  return statusMap[status] || status
}

const getProductReason = (productName: string): string => {
  const reasons: Record<string, string> = {
    'Show Flock Layer 22': 'High margin opportunity',
    'Strategy Healthy Edge': 'Competitive replacement',
    'Safe Choice Horse Feed': 'New product launch',
    'Ultium Growth': 'Inventory optimization'
  }
  return reasons[productName] || 'Strategic focus'
}

function onRefresh(done: () => void) {
  // Refresh the current route
  router.go(0); // This reloads the current route
  done();
}
</script>

/* Remove all background colors from root elements */
html {
  background: #ffffff;
}

body {
  background: #ffffff;
  margin: 0;
  padding: 0;
}