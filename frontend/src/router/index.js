import { createRouter, createWebHistory } from 'vue-router'
import AuthService from '@/services/AuthService'

const isDevMode = process.env.VUE_APP_DEV_MODE === 'true'

const routes = [
  // === ПУБЛИЧНЫЕ ===
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/LoginPage.vue')
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import('@/views/RegisterPage.vue')
    },

    // === ЗАЩИЩЁННЫЕ ===
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/HomePage.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/workout',
        name: 'Workout',
        component: () => import('@/views/WorkoutPage.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/choose_training',
        name: 'ChooseTraining',
        component: () => import('@/views/ChooseTraining.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/doing_exercises',
        name: 'DoingExercises',
        component: () => import('@/views/DoingExercises.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/rest',
        name: 'RestExercises',
        component: () => import('@/views/RestExercises.vue'),
        meta: { requiresAuth: true }
    },
    {
        path: '/end',
        name: 'EndExercises',
        component: () => import('@/views/EndExercises.vue'),
        meta: { requiresAuth: true }
    },

    // === УНИВЕРСАЛЬНЫЙ РЕДАКТОР ТРЕНИРОВОК ===
    {
        path: '/training/:id?/edit',
        name: 'TrainingEditor',
        component: () => import('@/views/TrainingEditor.vue'),
        meta: { requiresAuth: true }
    },

    // === РЕДИРЕКТЫ СО СТАРЫХ URL ===
    {
        path: '/make_training',
        redirect: '/training/edit'
    },
    {
        path: '/edit_training',
        redirect: to => {
        const id = to.query.id || ''
        return `/training/${id}/edit`
        }
    },
    {
    path: '/doing_exercises/:workoutId',
    name: 'DoingExercises',
    component: () => import('@/views/DoingExercises.vue'),
    meta: { requiresAuth: true }
    },
    {
    path: '/rest/:workoutId',
    name: 'RestExercises',
    component: () => import('@/views/RestExercises.vue'),
    meta: { requiresAuth: true }
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

// === ГЛОБАЛЬНАЯ ПРОВЕРКА АВТОРИЗАЦИИ ===
router.beforeEach(async (to, from, next) => {
    if (isDevMode) {
        return next()
    }

    if (to.meta.requiresAuth) {
        try {
        const user = await AuthService.getCurrentUser()
        if (user) {
            next()
        } else {
            next({ name: 'Login', query: { redirect: to.fullPath } })
        }
        } catch (error) {
        next({ name: 'Login' })
        }
    } else {
        next()
    }
})

export default router