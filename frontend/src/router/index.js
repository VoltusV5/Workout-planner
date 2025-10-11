import {createRouter, createWebHistory} from 'vue-router'
import HomePage from '../views/HomePage.vue'
import WorkoutPage from '../views/WorkoutPage.vue'

const routes = [
    {path: '/', name: 'Home', component: HomePage},
    { path: '/workout', name: 'Workout', component: WorkoutPage }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_YRL),
    routes
})

export default router

