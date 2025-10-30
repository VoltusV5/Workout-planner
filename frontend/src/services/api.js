// frontend/src/services/api.js

import axios from 'axios'
import AuthService from './AuthService'

const api = axios.create({
  baseURL: '/api/',
})

// === ИНТЕРЦЕПТОР ЗАПРОСОВ: ДОБАВЛЯЕМ ТОКЕН ===
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// === ИНТЕРЦЕПТОР ОТВЕТОВ: АВТО-ОБНОВЛЕНИЕ ТОКЕНА ===
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const refreshed = await AuthService.refreshToken()
      if (refreshed) {
        return api(originalRequest)
      }
    }
    return Promise.reject(error)
  }
)

// === МЕТОДЫ ===
export const getExercises = () => api.get('exercises/')
export const createExercise = (data) => api.post('exercises/', data)
export const updateExercise = (id, data) => api.put(`exercises/${id}/`, data)
export const deleteExercise = (id) => api.delete(`exercises/${id}/`)

export const getWorkouts = () => api.get('workouts/')
export const createWorkout = (data) => api.post('workouts/', data)
export const updateWorkout = (id, data) => api.put(`workouts/${id}/`, data)
export const deleteWorkout = (id) => api.delete(`workouts/${id}/`)


export default api