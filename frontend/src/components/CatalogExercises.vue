<template>
  <div class="CatalogExercises">
    <div class="CatalogExercises_header">
      <p>Каталог упражнений</p>
      <AddButton @click="showAddModal" />
    </div>

    <draggable
      :list="localExercises"
      group="exercises"
      @start="$emit('update:drag', true)"
      @end="$emit('update:drag', false)"
      @update="updateLocalExercises"
      class="ExerciseCards_Container"
    >
      <template #item="{ element }">
        <ExerciseCard
          :exercise="element"
          @edit="openEditModal"
          @delete="deleteExercise"
        />
      </template>

      <template #header>
        <div v-if="loading" class="loading">Загрузка...</div>
        <div v-else-if="localExercises.length === 0" class="empty">
          <h3>Нет упражнений</h3>
          <p>Добавьте первое упражнение!</p>
        </div>
      </template>
    </draggable>

    <AddExercise
      v-if="isModalVisible"
      :exercise="editingExercise"
      @close="closeModal"
      @save="handleSaveExercise"
    />
  </div>
</template>

<script>
import AddButton from './AddButton.vue'
import ExerciseCard from './ExerciseCard.vue'
import AddExercise from './AddExercise.vue'
import draggable from 'vuedraggable'
import { getExercises, createExercise, updateExercise, deleteExercise } from '@/services/api'

export default {
  name: 'CatalogExercises',
  components: { AddButton, ExerciseCard, AddExercise, draggable },
  props: { drag: Boolean },
  emits: ['update:catalogExercises', 'update:drag'],

  data() {
    return {
      localExercises: [],
      loading: false,
      isModalVisible: false,
      editingExercise: null
    }
  },

  watch: {
    localExercises: {
      handler(newVal) {
        this.$emit('update:catalogExercises', [...newVal])
      },
      deep: true
    }
  },

  async mounted() {
    await this.loadExercises()
  },

  methods: {
    async loadExercises() {
        this.loading = true
        try {
            console.log('Запрос: GET /api/exercises/')
            const response = await getExercises()
            console.log('Сырой ответ:', response.data)

            let exercises = []

            // ← КЛЮЧЕВОЕ: ПРОВЕРКА ПАГИНАЦИИ
            if (Array.isArray(response.data)) {
            exercises = response.data
            } else if (response.data && Array.isArray(response.data.results)) {
            exercises = response.data.results
            } else {
            console.warn('Неожиданный формат данных:', response.data)
            exercises = []
            }

            // Форматируем URL видео
            this.localExercises = exercises.map(ex => ({
            ...ex,
            video_file: ex.video_file
                ? `${process.env.VUE_APP_API_URL || ''}${ex.video_file}`
                : null
            }))

            this.$emit('update:catalogExercises', [...this.localExercises])
        } catch (error) {
            console.error('Ошибка загрузки:', error.response || error)
            const msg = error.response?.data?.detail || error.message || 'Сервер недоступен'
            alert('Не удалось загрузить упражнения: ' + msg)
        } finally {
            this.loading = false
        }
    },

    updateLocalExercises() {
      this.$emit('update:catalogExercises', [...this.localExercises])
    },

    showAddModal() {
      this.editingExercise = null
      this.isModalVisible = true
    },

    openEditModal(exercise) {
      this.editingExercise = { ...exercise }
      this.isModalVisible = true
    },

    closeModal() {
      this.isModalVisible = false
      this.editingExercise = null
    },

    async handleSaveExercise(formData) {
      try {
        if (this.editingExercise) {
          await updateExercise(this.editingExercise.id, formData)
        } else {
          await createExercise(formData)
        }
        await this.loadExercises()
        this.closeModal()
      } catch (error) {
        console.error('Ошибка сохранения:', error.response?.data || error)
        alert(
          'Ошибка: ' +
          (error.response?.data?.video_file?.[0] ||
           error.response?.data?.detail ||
           'Попробуйте снова')
        )
      }
    },

    async deleteExercise(id) {
      if (!confirm('Удалить упражнение?')) return
      try {
        await deleteExercise(id)
        this.localExercises = this.localExercises.filter(ex => ex.id !== id)
        this.$emit('update:catalogExercises', [...this.localExercises])
      } catch (error) {
        alert('Не удалось удалить')
      }
    }
  }
}
</script>

<style scoped>
.CatalogExercises {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 1250px;
  height: 819px;
  float: right;
  margin-right: 20px;
  background-color: #404040;
  border-radius: 48px;
  padding: 20px;
  box-sizing: border-box;
}

.CatalogExercises_header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin: 0 40px 40px 40px;
}

.CatalogExercises_header p {
  font-size: 90px;
  color: #fff;
  margin: 0;
}

.ExerciseCards_Container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  padding: 0 20px;
  overflow-y: auto;
  max-height: calc(819px - 180px);
  scrollbar-width: thin;
}

.loading, .empty {
  text-align: center;
  color: #aaa;
  padding: 40px;
  grid-column: 1 / -1;
}

.empty h3 { margin: 0 0 8px; }
.empty p { margin: 0; font-size: 18px; }


.ExerciseCards_Container {
    margin: 0px 10px 10px 10px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 20px;
    overflow-y: auto;
}


.CatalogExercises {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 1250px;
    height: 819px;
    float: right;
    margin-right: 20px;
    background-color: #404040;
    border-radius: 48px;
}

.CatalogExercises_header {
    display: flex;
    justify-content: space-between;
    text-align: center;
    margin: 0px 40px 60px 40px;
}

.CatalogExercises_header p {
    font-size: 90px;
    color: #fff;
    margin: 0;
    margin-right: 70px;
}



.Container_empty_alertInfo_catalogExercises {
    color: red;
    padding: 20px;
    font-size: 24px;
    border: 1px solid #ccc;
    border-bottom: 500px solid transparent;
    border-right: 1000px solid transparent;
}

.ExerciseCard {
    margin-bottom: 20px;
}

</style>