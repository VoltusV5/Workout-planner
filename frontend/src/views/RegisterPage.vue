<template>
    <div class="auth-container">
        <h2>Регистрация</h2>
        <form @submit.prevent="handleRegister">
        <div>
            <label for="username">Имя пользователя:</label>
            <input type="text" id="username" v-model="username" required />
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required />
        </div>
        <div>
            <label for="password">Пароль:</label>
            <input type="password" id="password" v-model="password" required />
        </div>
        <div>
            <button type="submit">Зарегистрироваться</button>
        </div>
        <p v-if="error" class="error">{{ error }}</p>
        </form>
        <p>Уже есть аккаунт? <router-link to="/login">Войти</router-link></p>
    </div>
</template>

<script>
import AuthService from '@/services/AuthService';

export default {
    data() {
        return {
        username: '',
        email: '',
        password: '',
        error: null,
        };
    },
    methods: {
        async handleRegister() {
        this.error = null;
        try {
            await AuthService.register(this.username, this.email, this.password);
            this.$router.push('/login');
        } catch (error) {
            this.error = error.error || error.detail || 'Что-то пошло не так';
        }
        },
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
