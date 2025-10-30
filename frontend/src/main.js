import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

let AuthService
if (process.env.VUE_APP_DEV_MODE === 'true') {
    AuthService = require('./services/AuthService.dev.js').default
    } else {
    AuthService = require('./services/AuthService.js').default
}

const app = createApp(App)
app.config.globalProperties.$auth = AuthService

app.use(router).mount('#app')