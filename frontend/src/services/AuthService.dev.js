export default {
    async login() {
        localStorage.setItem('access_token', 'dev-token')
        localStorage.setItem('refresh_token', 'dev-refresh')
        return { access: 'dev-token', refresh: 'dev-refresh' }
    },
    async getCurrentUser() {
        return { id: 1, username: 'dev-user', email: 'dev@example.com' }
    },
    logout() {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
    }
}