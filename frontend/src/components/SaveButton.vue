
<template>
  <div class="SaveButton">
    <!-- Основная разметка компонента -->
     <button>Сохранить</button>
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
    width: 425px;
    height: 153px;
    border-radius: 48px;
    font-size: 60px;
}

</style>
