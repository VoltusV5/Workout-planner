<!-- frontend/src/views/TrainingEditor.vue -->
<template>
  <div class="training-editor">
    <div class="header">
      <ArrowBack :action="isEdit ? 'goChooseTraining' : 'goHome'" />
      <h1>{{ isEdit ? 'Редактирование' : 'Создание' }} тренировки</h1>
      <SaveButton @click="saveWorkout" />
    </div>

    <!-- Ввод названия -->
    <input
      v-model="workoutName"
      placeholder="Введите название тренировки"
      class="name-input"
      :disabled="isEdit"
    />

    <!-- Каталог упражнений -->
    <CatalogExercises
      :catalogExercises="catalogExercises"
      @update:catalogExercises="catalogExercises = $event"
      @update:drag="updateDrag"
    />

    <!-- Твоя тренировка -->
    <YourTraining
      :YourTraining="trainingExercises"
      @update:YourTraining="updateTraining"
      @update:drag="updateDrag"
      :drag="drag"
    />
  </div>
</template>

<script>
import ArrowBack from '@/components/ArrowBack.vue'
import SaveButton from '@/components/SaveButton.vue'
import CatalogExercises from '@/components/CatalogExercises.vue'
import YourTraining from '@/components/YourTraining.vue'
import { createWorkout, getWorkouts } from '@/services/api'

export default {
  name: 'TrainingEditor',
  components: { ArrowBack, SaveButton, CatalogExercises, YourTraining },
  props: ['id'],

  data() {
    return {
      catalogExercises: [],
      trainingExercises: [],
      workoutName: '',
      drag: false,
      isEdit: false,
      workout: null
    }
  },

  async mounted() {
    this.isEdit = !!this.$route.params.id
    if (this.isEdit) {
      await this.loadWorkout()
    }
  },

  methods: {
    updateTraining(exercises) {
      this.trainingExercises = exercises
    },

    updateDrag(val) {
      this.drag = val
    },

    async loadWorkout() {
      try {
        const response = await getWorkouts()
        const workout = response.data.find(w => w.id == this.$route.params.id)
        if (workout) {
          this.workout = workout
          this.workoutName = workout.name
          this.trainingExercises = workout.exercises.map(e => ({
            ...e.exercise,
            order: e.order
          })).sort((a, b) => a.order - b.order)
        }
      } catch (error) {
        console.error('Ошибка загрузки тренировки:', error)
        alert('Не удалось загрузить тренировку')
      }
    },

    async saveWorkout() {
      if (!this.workoutName.trim()) {
        alert('Введите название тренировки')
        return
      }
      if (this.trainingExercises.length === 0) {
        alert('Добавьте хотя бы одно упражнение')
        return
      }

      const payload = {
        name: this.workoutName,
        workoutexercise_set: this.trainingExercises.map((ex, index) => ({
          exercise_id: ex.id,
          order: index
        }))
      }

      console.log('Сохраняем:', payload)

      try {
        let response
        if (this.isEdit && this.workout) {
          // TODO: updateWorkout(payload, this.workout.id)
          alert('Редактирование пока не реализовано')
          return
        } else {
          response = await createWorkout(payload)
        }

        console.log('Тренировка сохранена:', response.data)
        alert('Тренировка успешно сохранена!')
        this.$router.push('/workouts')
      } catch (error) {
        console.error('Ошибка сохранения:', error.response?.data)
        const msg = error.response?.data?.name?.[0] ||
                    error.response?.data?.non_field_errors?.[0] ||
                    'Не удалось сохранить тренировку'
        alert('Ошибка: ' + msg)
      }
    }
  }
}
</script>

<style scoped>
.training-editor {
    padding: 20px;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
</style>