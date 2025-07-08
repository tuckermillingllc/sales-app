import axios from 'axios'

const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:4173'
const API = axios.create({
  baseURL: `${baseURL}/api/v1`
})

export default API
