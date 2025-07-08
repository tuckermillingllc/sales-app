
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

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import API from '@/services/api'

// ✅ Define the customer type
interface Customer {
  id: number
  name: string
}

// ✅ Use the type in the ref
const customers = ref<Customer[]>([])

onMounted(async () => {
  const response = await API.get('/customers/')
  customers.value = response.data
})
</script>

