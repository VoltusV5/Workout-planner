
<template>
  <div class="AddButton">
    <!-- Основная разметка компонента -->
     <button>✓</button>
  </div>
</template>


<script>
export default {
  name: 'AddButton', // Название компонента

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
    background-color: #26CA7E;
    color: #fff;
    width: 110px;
    height: 110px;
    border-radius: 48px;
    font-size: 60px;
}

</style>
