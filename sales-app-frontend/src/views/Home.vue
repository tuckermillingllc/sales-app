<template>
  <div class="dashboard">
    <!-- Header Section -->
    <div class="header">
  <div class="header-content">
    <div class="brand-section">
      <div class="logo-container">
        <img :src="tuckerLogo" alt="Tucker Milling" class="company-logo" />
      </div>
      <div class="brand-text">
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
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import tuckerLogo from '@/assets/tucker-logo.png'

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
const totalDealers = ref(23)

// Sample data
const activeDealers = ref<Dealer[]>([
  { id: 1, name: 'Farmland Feed & Supply', status: 'active', metric: '+12%', metricType: 'positive' },
  { id: 2, name: 'Heritage Farm Supply', status: 'active', metric: '+15%', metricType: 'positive' },
  { id: 3, name: 'Country Store Co-op', status: 'active', metric: '+8%', metricType: 'positive' },
  { id: 4, name: 'Rural Feed Solutions', status: 'active', metric: '+5%', metricType: 'positive' }
])

const attentionDealers = ref<Dealer[]>([
  { id: 1, name: 'Valley Feed & Grain', status: 'declining', metric: '-25%', metricType: 'negative' },
  { id: 2, name: 'Prairie Farm Store', status: 'stopped', metric: '6 weeks', metricType: 'warning' },
  { id: 3, name: 'Midwest Ag Supply', status: 'declining', metric: '-15%', metricType: 'negative' },
  { id: 4, name: 'Sunset Feed Co.', status: 'stopped', metric: '4 weeks', metricType: 'warning' }
])

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

<style scoped>
/* CSS Custom Properties for consistent theming */
:root {
  --color-primary: #16a34a;
  --color-danger: #dc2626;
  --color-warning: #f59e0b;
  --color-info: #2563eb;
  --color-neutral: #6b7280;
  
  --color-text-primary: #1f2937;
  --color-text-secondary: #6b7280;
  --color-text-muted: #9ca3af;
  
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f9fafb;
  --color-bg-muted: #f3f4f6;
  
  --color-border: #e5e7eb;
  --color-border-light: #f3f4f6;
  
  --border-radius: 8px;
  --border-radius-lg: 12px;
  --border-radius-xl: 16px;
  
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 8px 25px rgba(0, 0, 0, 0.1);
  
  --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Base Styles */
html, body {
  background: var(--color-bg-primary);
  margin: 0;
  padding: 0;
}

.dashboard {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
  background: transparent;
  min-height: 100vh;
}

/* Header Section */
.header {
  background: var(--color-bg-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-xl);
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: var(--shadow-sm);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.company-logo {
  height: 6rem;
  width: auto;
  object-fit: contain;
}

.tagline {
  color: var(--color-text-secondary);
  font-size: 1.125rem;
  font-weight: 500;
  margin: 0;
}

/* Stats Overview Grid */
.stats-overview-grid {
  display: grid;
  grid-template-columns: repeat(2, auto);
  gap: 1.5rem 3rem;
  justify-content: start;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--color-text-primary);
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Dashboard Grid */
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.25rem;
}

/* Card Base Styles */
.dashboard-card {
  background: var(--color-bg-primary);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-lg);
  padding: 1.5rem;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: var(--shadow-sm);
  position: relative;
}

.dashboard-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-border-light);
}

/* Card Theme Variations */
.primary-card { border-left: 4px solid var(--color-primary); }
.warning-card { border-left: 4px solid var(--color-danger); }
.secondary-card { border-left: 4px solid var(--color-info); }
.accent-card { border-left: 4px solid var(--color-warning); }
.tertiary-card { border-left: 4px solid var(--color-neutral); }

/* Card Header */
.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 1.25rem;
  gap: 1rem;
}

.card-icon {
  width: 44px;
  height: 44px;
  border-radius: var(--border-radius);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-secondary);
}

.card-icon svg {
  width: 24px;
  height: 24px;
}

/* Icon Theme Colors */
.dealers-icon { background: #f0fdf4; color: var(--color-primary); }
.attention-icon { background: #fef2f2; color: var(--color-danger); }
.location-icon, .products-icon { background: #eff6ff; color: var(--color-info); }
.focus-icon { background: #fefbf0; color: var(--color-warning); }
.knowledge-icon, .competitive-icon, .selection-icon { background: var(--color-bg-secondary); color: var(--color-neutral); }

.card-title-section {
  flex: 1;
}

.card-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--color-text-primary);
  margin-bottom: 0.125rem;
}

.card-subtitle {
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  font-weight: 500;
}

.card-action svg {
  width: 20px;
  height: 20px;
  color: var(--color-text-muted);
}

/* Badges and Indicators */
.notification-badge, .priority-indicator {
  background: var(--color-danger);
  color: white;
  border-radius: 12px;
  padding: 0.25rem 0.625rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.trending-indicator {
  color: var(--color-primary);
}

.trending-indicator svg {
  width: 16px;
  height: 16px;
}

/* Metrics and Stats */
.metrics-row, .network-stats, .competitive-overview, .knowledge-stats {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1.25rem;
}

.metric, .coverage-item, .competitive-metric, .knowledge-metric {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.metric-value, .coverage-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--color-text-primary);
  line-height: 1;
  margin-bottom: 0.125rem;
}

.metric-value.positive, .coverage-value {
  color: var(--color-primary);
}

.metric-value.growth-positive {
  color: var(--color-primary);
}

.metric-label, .coverage-label {
  font-size: 0.75rem;
  color: var(--color-text-secondary);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Lists and Items */
.preview-list, .location-list, .priority-list, .recent-queries, .growth-products-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.list-item, .location-item, .priority-item, .ranking-item, .growth-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1rem;
  background: var(--color-bg-secondary);
  border-radius: var(--border-radius);
  border: 1px solid var(--color-border-light);
  gap: 0.75rem;
}

.item-content, .location-info, .priority-content, .product-details, .product-info {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.item-name, .location-name, .product-name {
  font-weight: 500;
  color: var(--color-text-primary);
  font-size: 0.875rem;
  margin-bottom: 0.125rem;
}

.item-location, .item-status, .location-address, .priority-reason, .product-category, .growth-period {
  font-size: 0.75rem;
  color: var(--color-text-secondary);
}

.item-status.declining {
  color: var(--color-warning);
}

.item-status.stopped {
  color: var(--color-danger);
}

/* Metric Badges */
.item-metric {
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
}

.item-metric.positive {
  background: #f0fdf4;
  color: var(--color-primary);
}

.item-metric.negative {
  background: #fef2f2;
  color: var(--color-danger);
}

.item-metric.warning {
  background: #fefbf0;
  color: var(--color-warning);
}

/* Alert Summary */
.alert-summary {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.25rem;
}

.alert-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.75rem;
  border-radius: var(--border-radius);
  flex: 1;
}

.alert-item.urgent {
  background: #fef2f2;
}

.alert-item.moderate {
  background: #fefbf0;
}

.alert-count {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-text-primary);
  margin-bottom: 0.125rem;
}

.alert-label {
  font-size: 0.75rem;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  font-weight: 500;
  letter-spacing: 0.05em;
  text-align: center;
}

/* Special Components */
.distance-badge {
  background: #eff6ff;
  color: var(--color-info);
  padding: 0.125rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.product-categories {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.category-pill {
  background: var(--color-bg-muted);
  color: var(--color-text-primary);
  padding: 0.375rem 0.75rem;
  border-radius: 16px;
  font-size: 0.75rem;
  font-weight: 500;
}

.priority-badge {
  font-size: 0.625rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.priority-badge.high {
  background: #fef2f2;
  color: var(--color-danger);
}

.priority-badge.medium {
  background: #fefbf0;
  color: var(--color-warning);
}

.query-item {
  padding: 0.5rem 0.75rem;
  background: var(--color-bg-secondary);
  border-radius: 6px;
  font-size: 0.875rem;
  color: var(--color-text-primary);
}

.replacement-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  background: var(--color-bg-secondary);
  border-radius: var(--border-radius);
  font-size: 0.875rem;
}

.competitor-name {
  color: var(--color-danger);
  font-weight: 500;
}

.replacement-arrow {
  color: var(--color-text-secondary);
}

.tucker-solution {
  color: var(--color-primary);
  font-weight: 500;
}

.selection-process {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.process-step {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  background: var(--color-bg-secondary);
  border-radius: 6px;
}

.step-indicator, .rank-indicator {
  width: 24px;
  height: 24px;
  background: var(--color-neutral);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
}

.step-label {
  font-size: 0.875rem;
  color: var(--color-text-primary);
  font-weight: 500;
}

/* Growth Indicators */
.growth-indicator-badge {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.375rem 0.625rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
}

.growth-indicator-badge svg {
  width: 12px;
  height: 12px;
}

.growth-indicator-badge.growth-high {
  background: #f0fdf4;
  color: var(--color-primary);
  border: 1px solid #bbf7d0;
}

.growth-indicator-badge.growth-medium {
  background: #fefbf0;
  color: var(--color-warning);
  border: 1px solid #fed7aa;
}

.growth-indicator-badge.growth-low {
  background: #fef2f2;
  color: var(--color-danger);
  border: 1px solid #fecaca;
}

.ranking-stats, .growth-summary {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.ranking-metric, .growth-metric {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sales-data {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.sales-volume {
  font-size: 0.75rem;
  color: var(--color-text-secondary);
}

.revenue-amount {
  font-weight: 600;
  color: var(--color-text-primary);
}

/* Responsive Design */
@media (max-width: 768px) {
  .dashboard {
    padding: 1rem;
  }
  
  .dashboard-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .header-content {
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
  }
  
  .brand-section {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .company-logo {
    height: 4.5rem;
  }
  
  .metrics-row, .network-stats, .competitive-overview, .knowledge-stats {
    flex-direction: column;
    gap: 1rem;
  }
  
  .stats-overview-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}

@media (max-width: 480px) {
  .company-logo {
    height: 3rem;
  }
  
  .alert-summary {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .product-categories {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .category-pill {
    text-align: center;
  }
}

/* Large screen optimizations */
@media (min-width: 1201px) {
  .dashboard-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>