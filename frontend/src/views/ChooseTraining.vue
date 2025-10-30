<!-- frontend/src/views/ChooseTraining.vue -->
<template>
    <div class="choose-training">
        <div class="header">
        <ArrowBack action="goHome" />
        <h1>Мои тренировки</h1>
        <router-link to="/training/edit">
            <AddButton />
        </router-link>
        </div>

        <div class="workouts-list">
        <div v-if="loading" class="loading">Загрузка...</div>
        <div v-else-if="workouts.length === 0" class="empty">
            <p>У вас нет тренировок</p>
            <router-link to="/training/edit">
            <button class="btn-create">Создать первую</button>
            </router-link>
        </div>
        <div v-else v-for="workout in workouts" :key="workout.id" class="workout-card">
            <h3>{{ workout.name }}</h3>
            <p>{{ workout.exercises.length }} упражнений</p>
            <div class="actions">
            <button @click="startWorkout(workout)" class="btn-start">Начать</button>
            <router-link :to="`/training/${workout.id}/edit`">
                <button class="btn-edit">Редактировать</button>
            </router-link>
            <button @click="deleteWorkout(workout.id)" class="btn-delete">Удалить</button>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
import ArrowBack from '@/components/ArrowBack.vue'
import AddButton from '@/components/AddButton.vue'
import { getWorkouts, deleteWorkout } from '@/services/api'

export default {
    components: { ArrowBack, AddButton },
    data() {
        return {
        workouts: [],
        loading: true
        }
    },
    async mounted() {
        await this.loadWorkouts()
    },
    methods: {
        async loadWorkouts() {
        this.loading = true
        try {
            const response = await getWorkouts()
            this.workouts = response.data
        } catch (error) {
            console.error('Ошибка загрузки тренировок:', error)
        } finally {
            this.loading = false
        }
        },
        startWorkout(workout) {
        this.$router.push({
            name: 'DoingExercises',
            params: { workoutId: workout.id }
        })
        },
        async deleteWorkout(id) {
        if (confirm('Удалить тренировку?')) {
            try {
            await deleteWorkout(id)
            this.workouts = this.workouts.filter(w => w.id !== id)
            } catch (error) {
            alert('Не удалось удалить')
            }
        }
        }
    }
}
</script>

<style scoped>
.choose-training {
    padding: 20px;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}
.workouts-list {
    display: grid;
    gap: 20px;
}
.workout-card {
    background: #2c2c2c;
    padding: 20px;
    border-radius: 16px;
    color: white;
}
.actions {
    margin-top: 12px;
    display: flex;
    gap: 10px;
}
.btn-start {
    background: #4CAF50;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
}
.btn-edit {
    background: #7C4DFF;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
}
.btn-delete {
    background: #f44336;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
}
.empty {
    text-align: center;
    color: #aaa;
    padding: 40px;
}
.btn-create {
    background: #7C4DFF;
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 12px;
    margin-top: 16px;
    font-size: 18px;
}
</style>