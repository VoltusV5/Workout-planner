<template>
  <div class="modal-overlay" @click="$emit('close')">
    <div class="modal" @click.stop>
      <h2>{{ exercise ? 'Редактировать' : 'Добавить' }} упражнение</h2>
      <form @submit.prevent="submit">
        <input v-model="form.name" placeholder="Название" required />
        <textarea v-model="form.description" placeholder="Описание" rows="3"></textarea>
        <input type="number" v-model.number="form.duration" placeholder="Длительность (сек)" required />
        <input type="number" v-model.number="form.repetitions" placeholder="Повторения" required />

        <input type="file" @change="onFileChange" accept="video/mp4" />
        <small v-if="form.video_file && typeof form.video_file === 'object'">
          Новый: {{ form.video_file.name }}
        </small>
        <small v-else-if="exercise?.video_file">
          Текущее: видео загружено
        </small>

        <div class="modal-actions">
          <button type="button" @click="$emit('close')">Отмена</button>
          <button type="submit" :disabled="isSubmitting">
            {{ isSubmitting ? 'Сохранение...' : 'Сохранить' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: ['exercise'],
  emits: ['close', 'save'],
  data() {
    return {
      form: {
        name: '',
        description: '',
        duration: 30,
        repetitions: 10,
        video_file: null
      },
      isSubmitting: false
    }
  },
  watch: {
    exercise: {
      immediate: true,
      handler(val) {
        if (val) {
          this.form = {
            name: val.name || '',
            description: val.description || '',
            duration: val.duration || 30,
            repetitions: val.repetitions || 10,
            video_file: null  // Новый файл, если нужно заменить
          }
        } else {
          this.resetForm()
        }
      }
    }
  },
  methods: {
    resetForm() {
      this.form = {
        name: '',
        description: '',
        duration: 30,
        repetitions: 10,
        video_file: null
      }
    },
    onFileChange(e) {
      const file = e.target.files[0]
      if (file) {
        this.form.video_file = file
      }
    },
    async submit() {
      if (this.isSubmitting) return
      this.isSubmitting = true

      const formData = new FormData()
      formData.append('name', this.form.name)
      formData.append('description', this.form.description)
      formData.append('duration', this.form.duration)
      formData.append('repetitions', this.form.repetitions)
      if (this.form.video_file) {
        formData.append('video_file', this.form.video_file)
      }

      this.$emit('save', formData)
      // Не сбрасываем форму здесь — ждём успешного ответа
    },
    // Вызывается родителем после успешного сохранения
    resetAfterSave() {
      this.isSubmitting = false
      this.resetForm()
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal {
  background: #1a1a1a;
  padding: 24px;
  border-radius: 16px;
  width: 90%;
  max-width: 500px;
  color: white;
}
input, textarea {
  width: 100%;
  padding: 12px;
  margin: 8px 0;
  border-radius: 8px;
  border: none;
  background: #333;
  color: white;
}
small {
  display: block;
  color: #aaa;
  margin: 4px 0 12px;
  font-size: 14px;
}
.modal-actions {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}
button {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
}
button[type="submit"] {
  background: #7C4DFF;
  color: white;
}
button:disabled {
  background: #555;
  cursor: not-allowed;
}
</style>