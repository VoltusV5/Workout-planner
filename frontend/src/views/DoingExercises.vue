<!-- frontend/src/views/DoingExercises.vue -->
<template>
  <div class="doing-exercises">
    <div class="header">
      <ArrowBack action="goChooseTraining" />
      <h1>Выполнение тренировки</h1>
    </div>

    <div v-if="loading" class="loading">Загрузка...</div>

    <div v-else-if="currentExercise" class="exercise-container">
      <!-- ВИДЕО -->
      <video
        :src="currentExercise.video_file"
        muted
        loop
        autoplay
        playsinline
        class="exercise-video"
      ></video>

      <!-- ИНФОРМАЦИЯ -->
      <div class="exercise-info">
        <h2>{{ currentExercise.name }}</h2>
        <p>{{ currentExercise.description }}</p>

        <!-- ТАЙМЕР -->
        <div class="timer">
          <div class="timer-circle" :style="{ '--progress': timerProgress }">
            <span>{{ formatTime(remainingTime) }}</span>
          </div>
        </div>

        <!-- ПОВТОРЕНИЯ -->
        <p class="repetitions">
          Повторения: {{ currentRep }} / {{ currentExercise.repetitions }}
        </p>

        <!-- ПРОГРЕСС-БАР -->
        <div class="progress-bar">
          <div
            class="progress-fill"
            :style="{ width: workoutProgress + '%' }"
          ></div>
        </div>
        <p class="progress-text">
          Упражнение {{ currentIndex + 1 }} из {{ totalExercises }}
        </p>

        <!-- КНОПКИ -->
        <div class="actions">
          <button @click="skipExercise" class="btn-skip">Пропустить</button>
          <button @click="pauseTimer" class="btn-pause">
            {{ isPaused ? 'Продолжить' : 'Пауза' }}
          </button>
        </div>
      </div>
    </div>

    <!-- КОНЕЦ ТРЕНИРОВКИ -->
    <div v-else-if="isFinished" class="finished">
      <h2>Тренировка завершена!</h2>
      <button @click="goToEnd" class="btn-finish">Перейти к результатам</button>
    </div>
  </div>
</template>

<script>
import ArrowBack from '@/components/ArrowBack.vue'
import { getWorkouts } from '@/services/api'

export default {
    name: 'DoingExercises',
    components: { ArrowBack },
    data() {
        return {
        workout: null,
        exercises: [],
        currentIndex: 0,
        currentRep: 1,
        remainingTime: 0,
        totalTime: 0,
        isPaused: false,
        isFinished: false,
        loading: true,
        timerInterval: null
        }
    },

    computed: {
        currentExercise() {
        return this.exercises[this.currentIndex] || null
        },
        totalExercises() {
        return this.exercises.length
        },
        workoutProgress() {
        if (!this.totalExercises) return 0
        const completed = this.currentIndex + (this.currentRep - 1) / this.currentExercise.repetitions
        return (completed / this.totalExercises) * 100
        },
        timerProgress() {
        return ((this.totalTime - this.remainingTime) / this.totalTime) * 100
        }
    },

    async mounted() {
        const workoutId = this.$route.params.workoutId
        if (!workoutId) {
        this.$router.push('/choose_training')
        return
        }
        await this.loadWorkout(workoutId)
        this.startExercise()
    },

    beforeUnmount() {
        if (this.timerInterval) clearInterval(this.timerInterval)
    },

    methods: {
        async loadWorkout(id) {
        this.loading = true
        try {
            const response = await getWorkouts()
            this.workout = response.data.find(w => w.id == id)
            if (this.workout) {
            this.exercises = this.workout.exercises
                .map(e => ({
                ...e.exercise,
                order: e.order
                }))
                .sort((a, b) => a.order - b.order)
            }
        } catch (error) {
            console.error('Ошибка загрузки тренировки:', error)
            this.$router.push('/choose_training')
        } finally {
            this.loading = false
        }
        },

        startExercise() {
        if (!this.currentExercise) return

        this.totalTime = this.currentExercise.duration
        this.remainingTime = this.totalTime

        this.timerInterval = setInterval(() => {
            if (!this.isPaused && this.remainingTime > 0) {
            this.remainingTime--
            }

            if (this.remainingTime <= 0) {
            this.nextRepOrExercise()
            }
        }, 1000)
        },

        nextRepOrExercise() {
        clearInterval(this.timerInterval)

        if (this.currentRep < this.currentExercise.repetitions) {
            this.currentRep++
            this.startExercise()
        } else if (this.currentIndex < this.totalExercises - 1) {
            this.currentIndex++
            this.currentRep = 1
            this.goToRest()
        } else {
            this.finishWorkout()
        }
        },

        goToRest() {
        clearInterval(this.timerInterval)
        this.$router.push({
            name: 'RestExercises',
            params: { workoutId: this.workout.id },
            query: { next: this.currentIndex }
        })
        },

        finishWorkout() {
        this.isFinished = true
        clearInterval(this.timerInterval)
        },

        goToEnd() {
        this.$router.push({
            name: 'EndExercises',
            params: { workoutId: this.workout.id }
        })
        },

        skipExercise() {
        this.nextRepOrExercise()
        },

        pauseTimer() {
        this.isPaused = !this.isPaused
        },

        formatTime(seconds) {
        const mins = Math.floor(seconds / 60).toString().padStart(2, '0')
        const secs = (seconds % 60).toString().padStart(2, '0')
        return `${mins}:${secs}`
        }
    }
}
</script>

<style scoped>
.doing-exercises {
    padding: 20px;
    color: white;
    min-height: 100vh;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.exercise-container {
    text-align: center;
}

.exercise-video {
    width: 100%;
    max-width: 600px;
    height: 340px;
    object-fit: cover;
    border-radius: 16px;
    margin: 0 auto 20px;
    display: block;
}

.exercise-info h2 {
    font-size: 36px;
    margin: 16px 0;
}

.exercise-info p {
    font-size: 18px;
    color: #ccc;
    margin: 8px 0;
}

.timer {
    margin: 30px 0;
}

.timer-circle {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    background: conic-gradient(#7C4DFF var(--progress, 0%), #333 var(--progress, 0%));
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
    font-size: 48px;
    font-weight: bold;
    position: relative;
}

.timer-circle span {
    background: #1a1a1a;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.repetitions {
    font-size: 24px;
    margin: 20px 0;
    color: #ff9800;
}

.progress-bar {
    width: 100%;
    max-width: 500px;
    height: 16px;
    background: #333;
    border-radius: 8px;
    margin: 20px auto;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: #7C4DFF;
    border-radius: 8px;
    transition: width 0.3s ease;
}

.progress-text {
    font-size: 16px;
    color: #aaa;
}

.actions {
    margin-top: 30px;
    display: flex;
    gap: 16px;
    justify-content: center;
}

.btn-skip, .btn-pause {
    padding: 12px 24px;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    cursor: pointer;
}

.btn-skip {
    background: #f44336;
    color: white;
}

.btn-pause {
    background: #ff9800;
    color: white;
}

.loading, .finished {
    text-align: center;
    padding: 60px;
    color: #aaa;
}

.btn-finish {
    margin-top: 20px;
    padding: 16px 32px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 16px;
    font-size: 20px;
}
</style>