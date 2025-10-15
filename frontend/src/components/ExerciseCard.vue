
<template>
  <div class="ExerciseCard">
    <!-- Основная разметка компонента -->
        <h3>Классический пресс</h3>
        <img class="ExerciseCard_image" src="../assets/make_training/image_card.png">
        <h5>40 сек</h5>
        <h6>x15 на каждую сторону</h6>
  </div>
</template>


<script>
export default {
  name: 'ExerciseCard', // Название компонента

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



.ExerciseCard {
    background-color: #D9D9D9;
    width: 256px;
    height: 256px;
    border-radius: 48px;
}

h3 {
    padding-top: 15px;
    padding-bottom: 10px;
    margin: 0px;
}

h5 {
    padding: 10px;
    margin: 0px;
    font-size: 30px
}

h6 {
    padding-bottom: 10px;
    margin: 0px;
    font-size: 15px
}

.ExerciseCard_image {
    width: 188px;
    height: 118px;
}

</style>
