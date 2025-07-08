<template>
  <div class="dashboard">
    <div class="header">
      <h1>Tucker Milling Sales</h1>
      <p>Your Animal's Choice - Dealer relationships and product knowledge</p>
    </div>

    <div class="cards-grid">
      <!-- Active Dealers -->
      <DashboardCard
        :card-data="{
          icon: '🏪',
          title: 'Active Dealers',
          subtitle: 'Top performing locations',
          type: 'dealers',
          items: activeDealers,
          badge: null,
          moreText: `View all ${totalDealers} dealers`
        }"
        @click="navigateTo('/dealers')"
      />

      <!-- Attention Needed -->
      <DashboardCard
        :card-data="{
          icon: '⚠️',
          title: 'Attention Needed',
          subtitle: 'Dealers requiring follow-up',
          type: 'attention',
          items: attentionDealers,
          badge: attentionCount,
          moreText: 'View all issues'
        }"
        @click="navigateTo('/attention')"
      />

      <!-- Dealer Locator -->
      <DashboardCard
        :card-data="{
          icon: '📍',
          title: 'Dealer Locator',
          subtitle: 'Find nearby dealers',
          type: 'locator',
          items: nearbyDealers,
          badge: null,
          moreText: 'View map & all locations'
        }"
        @click="navigateTo('/locator')"
      />

      <!-- Focus Products -->
      <DashboardCard
        :card-data="{
          icon: '🎯',
          title: 'Focus Products',
          subtitle: 'Priority products to push',
          type: 'focus',
          items: focusProducts,
          badge: null,
          moreText: 'View all focus products'
        }"
        @click="navigateTo('/focus')"
      />

      <!-- Product Catalog -->
      <DashboardCard
        :card-data="{
          icon: '🌾',
          title: 'Product Catalog',
          subtitle: 'Feed & nutrition guide',
          type: 'products',
          items: productCategories,
          badge: null,
          moreText: 'Browse all products'
        }"
        @click="navigateTo('/products')"
      />

      <!-- FAQ -->
      <DashboardCard
        :card-data="{
          icon: '❓',
          title: 'Product FAQ',
          subtitle: 'Quick nutrition answers',
          type: 'faq',
          items: frequentQuestions,
          badge: null,
          moreText: 'View all FAQs'
        }"
        @click="navigateTo('/faq')"
      />

      <!-- Competitive Replacements -->
      <DashboardCard
        :card-data="{
          icon: '🔄',
          title: 'Competitive Replacements',
          subtitle: 'Switch recommendations',
          type: 'comparison',
          items: competitiveReplacements,
          badge: null,
          moreText: 'View all replacements'
        }"
        @click="navigateTo('/comparison')"
      />

      <!-- Selection Tool -->
      <DashboardCard
        :card-data="{
          icon: '🎯',
          title: 'Selection Tool',
          subtitle: 'Feed recommendation wizard',
          type: 'selection',
          items: selectionSteps,
          badge: null,
          moreText: 'Start selection wizard'
        }"
        @click="navigateTo('/selection')"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import DashboardCard from '@/components/DashboardCard.vue'

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
  emoji?: string
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

// Router
const router = useRouter()

// Reactive data
const totalDealers = ref(23)

// Sample data (replace with API calls)
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
  { id: 3, name: 'Country Boy Feed Store', address: 'Arab, AL', distance: '22 mi' },
  { id: 4, name: 'Valley Feed & Supply', address: 'Decatur, AL', distance: '28 mi' }
])

const focusProducts = ref<Product[]>([
  { id: 1, name: 'Show Flock Layer 22', priority: 'high' },
  { id: 2, name: 'Strategy Healthy Edge', priority: 'high' },
  { id: 3, name: 'Safe Choice Horse Feed', priority: 'medium' },
  { id: 4, name: 'Ultium Growth', priority: 'medium' }
])

const productCategories = ref<Product[]>([
  { id: 1, name: 'Horse Feed', emoji: '🐴' },
  { id: 2, name: 'Cattle Feed', emoji: '🐄' },
  { id: 3, name: 'Poultry Feed', emoji: '🐔' },
  { id: 4, name: 'Swine Feed', emoji: '🐷' },
  { id: 5, name: 'Sheep Feed', emoji: '🐑' },
  { id: 6, name: 'Supplements', emoji: '🌾' }
])

const frequentQuestions = ref<Question[]>([
  { id: 1, question: 'Niacin in Show Flock Layer 22?' },
  { id: 2, question: 'Lowest NSC horse feed?' },
  { id: 3, question: 'Best feed for HYPP horses?' },
  { id: 4, question: 'Protein in Ultium Competition?' }
])

const competitiveReplacements = ref<Replacement[]>([
  { id: 1, competitor: 'Purina', competitorProduct: 'Strategy Healthy Edge', tuckerProduct: 'Easy Keeper 12' },
  { id: 2, competitor: 'Nutrena', competitorProduct: 'SafeChoice Senior', tuckerProduct: 'Senior Complete' },
  { id: 3, competitor: 'Triple Crown', competitorProduct: 'Senior Formula', tuckerProduct: 'Golden Years' }
])

const selectionSteps = ref([
  { id: 1, step: 'Animal type & life stage' },
  { id: 2, step: 'Nutritional requirements' },
  { id: 3, step: 'Get recommendations' }
])

// Computed
const attentionCount = computed(() => attentionDealers.value.length)

// Methods
const navigateTo = (path: string) => {
  console.log(`Navigating to: ${path}`)
  router.push(path)
}
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.header {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 24px;
  padding: 32px;
  margin-bottom: 32px;
  box-shadow: 
    0 4px 24px rgba(0, 0, 0, 0.06),
    0 1px 3px rgba(0, 0, 0, 0.08);
  position: relative;
  overflow: hidden;
}

.header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary-red), var(--primary-blue), var(--primary-green));
}

.header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--primary-red), var(--primary-blue));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
  text-align: center;
  letter-spacing: -0.02em;
}

.header p {
  text-align: center;
  color: var(--text-light);
  font-size: 1.1rem;
  font-weight: 400;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 24px;
}

@media (max-width: 768px) {
  .dashboard {
    padding: 16px;
  }
  
  .cards-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  
  .header {
    padding: 24px;
    margin-bottom: 24px;
  }
  
  .header h1 {
    font-size: 2rem;
  }
}

/* iOS-style animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.cards-grid > * {
  animation: fadeInUp 0.6s ease-out;
}

.cards-grid > *:nth-child(1) { animation-delay: 0.1s; }
.cards-grid > *:nth-child(2) { animation-delay: 0.2s; }
.cards-grid > *:nth-child(3) { animation-delay: 0.3s; }
.cards-grid > *:nth-child(4) { animation-delay: 0.4s; }
.cards-grid > *:nth-child(5) { animation-delay: 0.5s; }
.cards-grid > *:nth-child(6) { animation-delay: 0.6s; }
.cards-grid > *:nth-child(7) { animation-delay: 0.7s; }
.cards-grid > *:nth-child(8) { animation-delay: 0.8s; }
</style>