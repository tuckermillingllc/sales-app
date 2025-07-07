// frontend/src/components/CustomerCard.vue
<template>
  <div class="customer-card">
    <h3>{{ customer.name }}</h3>
    <p>Email: {{ customer.email }}</p>
    <p v-if="customer.phone">Phone: {{ customer.phone }}</p>
  </div>
</template>

<script setup>
defineProps({
  customer: Object,
})
</script>

<style scoped>
.customer-card {
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-bottom: 1rem;
  background-color: #f9f9f9;
}
</style>