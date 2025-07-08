<template>
  <div>
    <CustomerCard
      v-for="customer in customers"
      :key="customer.id"
      :customer="customer"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import CustomerCard from '@/components/CustomerCard.vue'
import API from '@/services/api'

interface Customer {
  id: number
  name: string
  email: string
  phone?: string  // optional if not all customers have phone numbers
}
const customers = ref<Customer[]>([])

onMounted(async () => {
  try {
    const response = await API.get('/customers/')
    customers.value = response.data
  } catch (error) {
    console.error('Failed to load customers:', error)
  }
})
</script>
