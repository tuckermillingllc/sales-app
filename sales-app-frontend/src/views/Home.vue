<script setup lang="ts">

</script>

<template>
  <div>
    <CustomerCard v-for="customer in customers" :key="customer.id" :customer="customer" />
  </div>
</template>