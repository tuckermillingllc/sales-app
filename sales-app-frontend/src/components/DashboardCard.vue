<template>
  <div 
    class="dashboard-card"
    :class="`card-${cardData.type}`"
    @click="$emit('click')"
  >
    <div class="card-header">
      <div class="card-icon">{{ cardData.icon }}</div>
      <div class="card-title-section">
        <div class="card-title">
          {{ cardData.title }}
          <span v-if="cardData.badge" class="notification-badge">
            {{ cardData.badge }}
          </span>
        </div>
        <div class="card-subtitle">{{ cardData.subtitle }}</div>
      </div>
    </div>
    
    <div class="card-content">
      <!-- Regular List Items -->
      <ul v-if="cardData.type !== 'products' && cardData.type !== 'selection'" class="preview-list">
        <li 
          v-for="item in cardData.items" 
          :key="item.id"
          class="preview-item"
          :class="getItemClass(item)"
        >
          <div class="item-info">
            <div 
              v-if="cardData.type === 'dealers' || cardData.type === 'attention'"
              class="status-indicator"
              :class="`status-${item.status}`"
            ></div>
            <div class="item-name">
              {{ getItemDisplayName(item) }}
            </div>
            <div v-if="cardData.type === 'locator'" class="location-address">
              {{ item.address }}
            </div>
          </div>
          
          <!-- Item Metrics/Actions -->
          <div v-if="hasMetric(item)" class="item-metric" :class="`metric-${item.metricType}`">
            {{ item.metric }}
          </div>
          <div v-else-if="cardData.type === 'focus'" class="priority-badge" :class="`priority-${item.priority}`">
            {{ item.priority?.toUpperCase() }}
          </div>
          <div v-else-if="cardData.type === 'locator'" class="location-distance">
            {{ item.distance }}
          </div>
        </li>
      </ul>

      <!-- Product Grid -->
      <div v-if="cardData.type === 'products'" class="product-grid">
        <div 
          v-for="item in cardData.items" 
          :key="item.id"
          class="product-category"
        >
          <span class="category-emoji">{{ item.emoji }}</span>
          <div class="category-name">{{ item.name }}</div>
        </div>
      </div>

      <!-- Selection Steps -->
      <div v-if="cardData.type === 'selection'" class="selection-steps">
        <div 
          v-for="(item, index) in cardData.items" 
          :key="item.id"
          class="step-container"
        >
          <div class="step-number">{{ index + 1 }}</div>
          <div class="step-text">{{ item.step }}</div>
        </div>
      </div>

      <!-- Competitive Replacements -->
      <template v-if="cardData.type === 'comparison'">
        <div 
          v-for="item in cardData.items" 
          :key="item.id"
          class="competitive-item"
        >
          <div>
            <div class="competitor-brand">{{ item.competitor }}</div>
            <div class="item-name">{{ item.competitorProduct }}</div>
          </div>
          <div class="replacement-arrow">→</div>
          <div>
            <div class="tucker-brand">Tucker Milling</div>
            <div class="item-name">{{ item.tuckerProduct }}</div>
          </div>
        </div>
      </template>

      <div class="more-indicator">{{ cardData.moreText }} →</div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface CardData {
  icon: string
  title: string
  subtitle: string
  type: string
  items: any[]
  badge: number | null
  moreText: string
}

defineProps<{
  cardData: CardData
}>()

defineEmits<{
  click: []
}>()

const getItemClass = (item: any) => {
  if (item.type === 'locator') return 'dealer-location'
  if (item.type === 'comparison') return 'competitive-item'
  return 'preview-item'
}

const getItemDisplayName = (item: any) => {
  if (item.question) return item.question
  return item.name
}

const hasMetric = (item: any) => {
  return item.metric && (item.metricType === 'positive' || item.metricType === 'negative' || item.metricType === 'warning')
}
</script>

<style scoped>
.dashboard-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 20px;
  padding: 24px;
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.08),
    0 1px 3px rgba(0, 0, 0, 0.12);
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.dashboard-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--accent-color);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.dashboard-card:hover::before {
  transform: scaleX(1);
}

.dashboard-card:hover {
  transform: translateY(-4px);
  box-shadow: 
    0 20px 48px rgba(0, 0, 0, 0.12),
    0 8px 16px rgba(0, 0, 0, 0.08);
}

.dashboard-card:active {
  transform: translateY(-2px);
  transition: transform 0.1s ease;
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.card-icon {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  margin-right: 16px;
  background: var(--accent-color);
  color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.card-title-section {
  flex: 1;
}

.card-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--text-dark);
  margin-bottom: 4px;
  letter-spacing: -0.01em;
}

.card-subtitle {
  color: var(--text-light);
  font-size: 0.9rem;
  font-weight: 400;
}

.card-content {
  color: #374151;
  line-height: 1.6;
}

.preview-list {
  list-style: none;
}

.preview-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  margin-bottom: 8px;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 12px;
  transition: all 0.2s ease;
  border: 1px solid rgba(226, 232, 240, 0.8);
}

.preview-item:hover {
  background: rgba(241, 245, 249, 0.9);
  transform: translateX(2px);
}

.preview-item:last-child {
  margin-bottom: 0;
}

.item-info {
  display: flex;
  align-items: center;
  flex: 1;
}

.status-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin-right: 12px;
  box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.8);
}

.item-name {
  font-weight: 500;
  color: var(--text-dark);
  font-size: 0.9rem;
}

.location-address {
  font-size: 0.8rem;
  color: var(--text-light);
  margin-left: 12px;
}

.item-metric {
  font-size: 0.8rem;
  font-weight: 500;
  padding: 4px 8px;
  border-radius: 6px;
  white-space: nowrap;
}

.location-distance {
  font-size: 0.8rem;
  color: var(--primary-blue);
  font-weight: 500;
  padding: 4px 8px;
  background: rgba(30, 58, 138, 0.1);
  border-radius: 6px;
}

.more-indicator {
  color: var(--primary-blue);
  font-size: 0.8rem;
  font-weight: 500;
  margin-top: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  background: rgba(30, 58, 138, 0.1);
  border-radius: 8px;
}

.notification-badge {
  background: var(--primary-red);
  color: white;
  border-radius: 10px;
  padding: 4px 8px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-left: 8px;
  box-shadow: 0 2px 4px rgba(196, 30, 58, 0.3);
}

.priority-badge {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.priority-high {
  background: #fef2f2;
  color: var(--primary-red);
  border: 1px solid #fecaca;
}

.priority-medium {
  background: #fef3c7;
  color: var(--accent-gold);
  border: 1px solid #fed7aa;
}

/* Tucker Milling Brand Card Colors */
.card-dealers { --accent-color: var(--primary-green); }
.card-attention { --accent-color: var(--primary-red); }
.card-focus { --accent-color: var(--accent-gold); }
.card-products { --accent-color: var(--primary-blue); }
.card-faq { --accent-color: var(--accent-gold); }
.card-comparison { --accent-color: var(--primary-blue); }
.card-selection { --accent-color: var(--primary-green); }
.card-locator { --accent-color: var(--primary-red); }

.status-active { background: var(--primary-green); }
.status-declining { background: var(--accent-gold); }
.status-stopped { background: var(--primary-red); }

.metric-positive {
  background: #dcfce7;
  color: var(--primary-green);
}

.metric-negative {
  background: #fee2e2;
  color: var(--primary-red);
}

.metric-warning {
  background: #fef3c7;
  color: var(--accent-gold);
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-top: 16px;
}

.product-category {
  background: rgba(248, 250, 252, 0.8);
  border: 1px solid rgba(226, 232, 240, 0.8);
  border-radius: 12px;
  padding: 16px;
  text-align: center;
  transition: all 0.2s ease;
}

.product-category:hover {
  background: rgba(241, 245, 249, 0.9);
  transform: translateY(-1px);
}

.category-emoji {
  font-size: 24px;
  margin-bottom: 8px;
  display: block;
}

.category-name {
  font-size: 0.9rem;
  font-weight: 500;
  color: #374151;
}

.competitive-item {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  margin-bottom: 8px;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 12px;
  border: 1px solid rgba(226, 232, 240, 0.8);
}

.competitor-brand {
  font-size: 0.7rem;
  color: var(--primary-red);
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 2px;
}

.tucker-brand {
  font-size: 0.7rem;
  color: var(--primary-green);
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 2px;
}

.replacement-arrow {
  margin: 0 12px;
  color: var(--text-light);
  font-size: 14px;
}

.step-container {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  margin-bottom: 8px;
  background: rgba(248, 250, 252, 0.8);
  border-radius: 12px;
  border: 1px solid rgba(226, 232, 240, 0.8);
}

.step-number {
  width: 24px;
  height: 24px;
  border-radius: 6px;
  background: var(--accent-color);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.8rem;
  margin-right: 12px;
}

.step-text {
  flex: 1;
  font-size: 0.9rem;
  font-weight: 500;
  color: #374151;
}

.selection-steps {
  margin-top: 16px;
}

@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>