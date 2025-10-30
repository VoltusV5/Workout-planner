<!-- frontend/src/components/ExerciseCard.vue -->
<template>
  <div class="exercise-card">
    <!-- Заголовок -->
    <h3 class="title">{{ exercise.name }}</h3>
    <p class="description">{{ exercise.description || 'Нет описания' }}</p>

    <!-- Видео -->
    <video
      v-if="exercise.video_file"
      :src="exercise.video_file"
      muted
      loop
      autoplay
      playsinline
      class="video"
    ></video>

    <!-- Мета -->
    <div class="meta">
      <span>Длительность: {{ exercise.duration }} сек</span>
      <span>Повторения: {{ exercise.repetitions }}</span>
    </div>

    <!-- Кнопки -->
    <div class="actions" v-if="$parent.$parent.showActions">
      <button @click="$emit('edit', exercise)" class="btn edit">Редактировать</button>
      <button @click="$emit('delete', exercise.id)" class="btn delete">Удалить</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExerciseCard',
  props: {
    exercise: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
/* === КАРТОЧКА === */
.exercise-card {
  background: #2c2c2c;
  border-radius: 16px;
  padding: 16px;
  color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  width: 280px;           /* ФИКСИРОВАННАЯ ШИРИНА */
  height: auto;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease;
}

.exercise-card:hover {
  transform: translateY(-4px);
}

/* === ТЕКСТ === */
.title {
  margin: 0 0 8px;
  font-size: 18px;
  font-weight: 600;
}

.description {
  margin: 0 0 12px;
  font-size: 14px;
  color: #ccc;
  flex-grow: 1;
}

/* === ВИДЕО === */
.video {
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: 12px;
  margin: 8px 0;
  background: #000;
}

/* === МЕТА === */
.meta {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #7C4DFF;
  margin: 8px 0;
}

/* === КНОПКИ === */
.actions {
  display: flex;
  gap: 8px;
  margin-top: auto;
}

.btn {
  flex: 1;
  padding: 8px 12px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: opacity 0.2s;
}

.btn:hover { opacity: 0.9; }

.edit { background: #7C4DFF; color: white; }
.delete { background: #f44336; color: white; }

/* === АДАПТИВНОСТЬ === */
@media (max-width: 768px) {
  .exercise-card { width: 100%; max-width: 300px; }
}
</style>