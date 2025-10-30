
import axios from 'axios';

const API_URL = '/api/';

class AuthService {
    // ЛОГИН - JWT TokenObtainPairView
    async login(username, password) {
        try {
        const response = await axios.post(`${API_URL}token/`, {
            username,
            password,
        });
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        return response.data;
        } catch (error) {
        console.error('Login error:', error.response?.data);
        throw error.response?.data || { detail: 'Login failed' };
        }
    }

    // РЕГИСТРАЦИЯ
    async register(username, email, password) {
        try {
        const response = await axios.post(`${API_URL}register/`, {
            username,
            email,
            password,
        });
        return response.data;
        } catch (error) {
        console.error('Register error:', error.response?.data);
        throw error.response?.data || { error: 'Registration failed' };
        }
    }

    // ПОЛЬЗОВАТЕЛЬ
    async getCurrentUser() {
        const token = localStorage.getItem('access_token')
        if (!token) return null
        try {
            const response = await axios.get('/api/user/', {
            headers: { Authorization: `Bearer ${token}` }
            })
            return response.data
        } catch (error) {
            if (error.response?.status === 401) this.logout()
            return null
        }
    }

    logout() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
    }
}

export default new AuthService();