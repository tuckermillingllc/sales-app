// frontend/src/views/Customers.vue
<template>
  <div>
    <h2>Customers</h2>
    <CustomerCard v-for="cust in customers" :key="cust.id" :customer="cust" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CustomerCard from '@/components/CustomerCard.vue'
import api from '@/services/api'

const customers = ref([])

onMounted(async () => {
  try {
    const response = await api.get('/customers')
    customers.value = response.data
  } catch (error) {
    console.error('Failed to load customers:', error)
  }
})
</script>
