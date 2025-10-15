
<template>
    <div>
        <div class="modal-overlay" @click="hideModal"></div>
        
        <div class="AddExercise">
            <div class="header_training_page">
                <ArrowBack action="closeModal" @close="hideModal" />
                <h1>Добавить упражнение</h1>
                <ApplyButton />
            </div>
            <input class="header_training_page_ClassicInput" type="text" placeholder="Введите название упражнения">
            <input class="header_training_page_VideoInput" type="text" placeholder="Загрузите видео">
            <input class="header_training_page_ClassicInput" type="text" placeholder="Введите кол-во секунд / кол-во повторений">
            <input class="header_training_page_ClassicInput" type="text" placeholder="Введите описание">
        </div>
    </div>
</template>


<script>
import ApplyButton from './ApplyButton.vue';
import ArrowBack from './ArrowBack.vue';

export default {
    name: 'AddExercise',
    components: {
        ArrowBack,
        ApplyButton
    },
    methods: {
        hideModal() {
        this.$emit('close');
        }
    },
};
</script>

<style scoped>

.header_training_page {
    width: 690px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 0 0 20px 0;
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 999;
}

.AddExercise {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -38%);
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 900px;
    height: 870px;
    background-color: #7C4DFF;
    border-radius: 48px 48px 0px 0px;
    z-index: 1000;
}

.header_training_page h1 {
    font-size: 40px;
    color: #fff;
}

.header_training_page_ClassicInput {
    height: 81px;
    width: 690px;
}

.header_training_page_VideoInput {
    height: 418px;
    width: 690px;
}

input {
    border-radius: 24px;
    margin-bottom: 15px;
    font-size: 30px;
    padding-left: 30px;
}

</style>
