<template>
  <div>
    <h2>Customers</h2>
    <ul>
      <li v-for="customer in customers" :key="customer.id">
        {{ customer.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import API from '@/services/api'

const customers = ref([])

onMounted(async () => {
  try {
    const response = await API.get('/customers/')
    customers.value = response.data
  } catch (error) {
    console.error('Failed to load customers:', error)
  }
})
</script>
