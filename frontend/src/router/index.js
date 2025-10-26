import {createRouter, createWebHistory} from 'vue-router'
import HomePage from '../views/HomePage.vue'
import WorkoutPage from '../views/WorkoutPage.vue'
import MakeTraining from '../views/MakeTraining.vue'
import ChooseTraining from '@/views/ChooseTraining.vue'
import EditTraining from '@/views/EditTraining.vue'
import DoingExercises from '@/views/DoingExercises.vue'
import RestExercises from '@/views/RestExercises.vue'
import EndExercises from '@/views/EndExercises.vue'

const routes = [
    {path: '/', name: 'Home', component: HomePage},
    { path: '/workout', name: 'Workout', component: WorkoutPage },
    { path: '/make_training', name: 'MakeTraining', component: MakeTraining },
    { path: '/choose_training', name: 'ChooseTraining', component: ChooseTraining },
    { path: '/edit_training', name: 'EditTraining', component: EditTraining },
    { path: '/doing_exercises', name: 'DoingExercises', component: DoingExercises },
    { path: '/rest', name: 'RestExercises', component: RestExercises },
    { path: '/end', name: 'EndExercises', component: EndExercises },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_YRL),
    routes
})

export default router

