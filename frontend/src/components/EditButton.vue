
<template>
    <div class="EditButton">
        <!-- Основная разметка компонента -->
            <button>Редактировать</button>
    </div>
</template>


<script>
export default {
  name: 'EditButton', // Название компонента

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
    width: 400px;
    height: 100px;
    border-radius: 48px;
    font-size: 40px;
    margin-top: 10px;
}

</style>
