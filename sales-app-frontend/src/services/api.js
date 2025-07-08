import axios from 'axios'

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL + '/api/v1/' || 'http://localhost:4173/api/v1'
})

export default API
