<template>
  <div class="your-training">
    <h2>Ваша тренировка</h2>

    <draggable
      :list="localExercises"
      group="exercises"
      @start="$emit('update:drag', true)"
      @end="$emit('update:drag', false)"
      @update="updateLocalExercises"
    >
      <!-- ОБЯЗАТЕЛЬНЫЙ СЛОТ #item -->
      <template #item="{ element }">
        <ExerciseCard
          :exercise="element"
          @delete="removeExercise(element.id)"
        />
      </template>

      <!-- Пустое состояние -->
      <template #header>
        <p v-if="localExercises.length === 0" class="empty">
          Перетащите упражнения сюда
        </p>
      </template>
    </draggable>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
import ExerciseCard from './ExerciseCard.vue'

export default {
  components: { draggable, ExerciseCard },
  props: {
    YourTraining: {
      type: Array,
      default: () => []
    }
  },
  emits: ['update:YourTraining', 'update:drag'],

  data() {
    return {
      localExercises: []
    }
  },

  watch: {
    YourTraining: {
      immediate: true,
      handler(newVal) {
        this.localExercises = [...newVal]
      }
    }
  },

  methods: {
    updateLocalExercises() {
      this.$emit('update:YourTraining', this.localExercises)
    },

    removeExercise(id) {
      this.localExercises = this.localExercises.filter(ex => ex.id !== id)
      this.$emit('update:YourTraining', this.localExercises)
    }
  }
}
</script>

<style scoped>
.Your_Training {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 412px;
    height: 819px;
    margin-left: 20px;
    background-color: #7C4DFF;
    border-radius: 48px;
}

.Your_Training p {
    font-size: 50px;
    color: white;
    margin: 20px 20px 20px 20px;
}

.Your_Training-ExerciseCards_Container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    overflow-y: auto;
    width: 100%;
    min-width: 120px;
    min-height: 720px;
}


.Container_empty_alertInfo_ExerciseCards_Container {
    color: red;
    padding: 20px;
    font-size: 24px;
    border: 1px solid #ccc;
    border-bottom: 600px solid transparent;
}



.ExerciseCard {
    margin-bottom: 20px;
}
</style>
