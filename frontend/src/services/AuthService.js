// frontend/src/services/AuthService.js

import api from './api'  // ← КЛЮЧЕВОЕ: используем api.js с интерцепторами

class AuthService {
  // === ЛОГИН ===
  async login(username, password) {
    try {
      const response = await api.post('token/', { username, password })
      localStorage.setItem('access_token', response.data.access)
      localStorage.setItem('refresh_token', response.data.refresh)
      console.log('Логин успешен, токен сохранён')
      return response.data
    } catch (error) {
      console.error('Ошибка логина:', error.response?.data)
      throw error.response?.data || { detail: 'Login failed' }
    }
  }

  // === РЕГИСТРАЦИЯ ===
  async register(username, email, password) {
    try {
      const response = await api.post('register/', { username, email, password })
      return response.data
    } catch (error) {
      console.error('Ошибка регистрации:', error.response?.data)
      throw error.response?.data || { error: 'Registration failed' }
    }
  }

  // === ПОЛЬЗОВАТЕЛЬ ===
  async getCurrentUser() {
    const token = localStorage.getItem('access_token')
    if (!token) return null

    try {
      const response = await api.get('user/')
      return response.data
    } catch (error) {
      if (error.response?.status === 401) {
        console.warn('Токен недействителен, выход...')
        this.logout()
      }
      return null
    }
  }

  // === ОБНОВЛЕНИЕ ТОКЕНА ===
  async refreshToken() {
    const refresh = localStorage.getItem('refresh_token')
    if (!refresh) return false

    try {
      const response = await api.post('token/refresh/', { refresh })
      localStorage.setItem('access_token', response.data.access)
      console.log('Токен обновлён')
      return true
    } catch (error) {
      console.error('Не удалось обновить токен:', error.response?.data)
      this.logout()
      return false
    }
  }

  // === ВЫХОД ===
  logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    console.log('Выход выполнен')
  }
}

export default new AuthService()