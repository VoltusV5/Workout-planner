<template>
    <div class="auth-container">
        <h2>Вход</h2>
        <form @submit.prevent="handleLogin">
        <div>
            <label for="username">Имя пользователя:</label>
            <input type="text" id="username" v-model="username" required />
        </div>
        <div>
            <label for="password">Пароль:</label>
            <input type="password" id="password" v-model="password" required />
        </div>
        <div>
            <button type="submit">Войти</button>
        </div>
        <p v-if="error" class="error">{{ error }}</p>
        </form>
        <p>Нет аккаунта? <router-link to="/register">Зарегистрироваться</router-link></p>


        <!-- КНОПКА ДЛЯ DEV -->
        <div v-if="$route.query.dev" style="margin-top: 20px; text-align: center;">
            <button @click="devLogin" style="background: #ff9800; color: white; padding: 10px;">
                DEV LOGIN (автовход)
            </button>
        </div>
    </div>
</template>

<script>
import AuthService from '@/services/AuthService'; 

export default {
    data() {
        return {
        username: '',
        password: '',
        error: null,
        };
    },
    methods: {
        async handleLogin() {
            try {
                await AuthService.login(this.username, this.password)
                const redirect = this.$route.query.redirect || '/'
                this.$router.push(redirect)
            } catch (error) {
                this.error = error.detail || 'Ошибка входа'
            }
        },

        async devLogin() {
            if (process.env.VUE_APP_DEV_MODE === 'true') {
                await this.$auth.login()
                this.$router.push(this.$route.query.redirect || '/')
            }
        }
    },
};
</script>

<style scoped>
.auth-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}

h2 {
    text-align: center;
}

input {
    width: 100%;
    padding: 8px;
    margin: 8px 0;
    border-radius: 4px;
    border: 1px solid #ccc;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
}

button:hover {
    background-color: #45a049;
}

.error {
    color: red;
    font-size: 14px;
}
</style>
