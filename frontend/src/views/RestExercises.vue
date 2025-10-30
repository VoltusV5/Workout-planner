<template>
    <div class="rest">
        <h1>Отдых</h1>
        <div class="timer">{{ formatTime(remaining) }}</div>
        <button @click="continueWorkout" class="btn-continue">Продолжить</button>
    </div>
</template>

<script>
export default {
    data() {
        return { remaining: 30, interval: null }
    },
    mounted() {
        this.interval = setInterval(() => {
        if (this.remaining > 0) this.remaining--
        else this.continueWorkout()
        }, 1000)
    },
    beforeUnmount() {
        clearInterval(this.interval)
    },
    methods: {
        continueWorkout() {
        clearInterval(this.interval)
        this.$router.push({
            name: 'DoingExercises',
            params: { workoutId: this.$route.params.workoutId }
        })
        },
        formatTime(s) {
        return `${Math.floor(s/60)}:${(s%60).toString().padStart(2,'0')}`
        }
    }
}
</script>

<style scoped>
.rest { text-align: center; padding: 60px; color: white; }
.timer { font-size: 72px; margin: 40px; }
.btn-continue { padding: 16px 32px; background: #4CAF50; color: white; border: none; border-radius: 16px; font-size: 20px; }
</style>