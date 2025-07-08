<template>
  <div class="customer-card">
    <h3>{{ customer.name }}</h3>
    <p>Email: {{ customer.email }}</p>
    <p v-if="customer.phone">Phone: {{ customer.phone }}</p>
  </div>
</template>

<script setup lang="ts">
interface Customer {
  id: number
  name: string
  email: string
  phone?: string
}

defineProps<{
  customer: Customer
}>()
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
