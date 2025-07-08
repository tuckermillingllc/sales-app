<template>
  <f7-page name="home" class="home-page">
    <f7-navbar title="Sales App" />

    <f7-block class="text-align-center intro-block">
      <h2 class="intro-title">Welcome</h2>
      <p class="intro-subtitle">Select a tool below</p>
    </f7-block>

    <f7-list strong inset dividers>
      <f7-card v-for="tool in tools" :key="tool.path" class="nav-card">
        <f7-card-content padding>
          <f7-button fill large class="card-button" @click="$router.push(tool.path)">
            {{ tool.label }}
          </f7-button>
        </f7-card-content>
      </f7-card>
    </f7-list>
  </f7-page>
</template>

<script setup lang="ts">
const tools = [
  { label: 'Product Info', path: '/products/' },
  { label: 'Promotions', path: '/promotions/' },
  { label: 'Technical Info', path: '/tech/' },
  { label: 'Product Chooser', path: '/choose/' },
  { label: 'Dealer Locator', path: '/locator/' },
]
</script>

<style scoped>
.home-page {
  background-color: #f2f2f7;
}

.intro-block {
  margin-top: 32px;
  margin-bottom: 16px;
}

.intro-title {
  font-size: 22px;
  font-weight: 600;
  color: #1c1c1e;
}

.intro-subtitle {
  font-size: 16px;
  color: #6e6e73;
}

.nav-card {
  margin-bottom: 12px;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.card-button {
  width: 100%;
  height: 48px;
  font-size: 16px;
  font-weight: 500;
}
</style>
