
<template>
  <div class="SaveButton">
    <!-- Основная разметка компонента -->
        <button><img src="../assets/make_training/Arrow.png" class="mirrored" /></button>
  </div>
</template>


<script>
export default {
  name: 'SaveButton', // Название компонента

  props: {
    // Пропсы, которые передаются в компонент
  },

  data() {
    return {
      // Локальное состояние компонента
    };
  },

  methods: {
    // Методы компонента
  },
};
</script>

<style scoped>

button {
    background-color: #7C4DFF;
    color: #fff;
    width: 300px;
    height: 100px;
    border-radius: 48px;
    font-size: 60px;
}

.mirrored {
  transform: scaleX(-1);  /* Отзеркаливает изображение по горизонтали */
}

</style>
