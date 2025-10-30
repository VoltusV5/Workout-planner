import axios from 'axios';
import AuthService from './AuthService';

const api = axios.create({
    baseURL: '/api/',
    });

    // Авто-обновление токена при 401
    api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if (error.response?.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        const refreshed = await AuthService.refreshToken();
        if (refreshed) {
            return api(originalRequest);
        }
        }
        return Promise.reject(error);
    }
);

export default api;