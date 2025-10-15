
<template>
    <div class="make_training_page">
        <div class="header_training_page">
            <ArrowBack action="goHome" />
            <h1>Создание тренировки</h1>
            <SaveButton />
        </div>
        <div class="CatalogExercises">
            <div class="CatalogExercises_header">
                <p>Каталог упражнений</p>
                <AddButton @click="showModal" />
            </div>
            
            <div class="ExerciseCards_Container">
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
            </div>
        </div>
        <div class="Your_Training">
            <p>Тренировка №1</p>
            <div class="Your_Training-ExerciseCards_Container">
                <ExerciseCard />
                <ExerciseCard />
                <ExerciseCard />
            </div>
        </div>
    
        <AddExercise v-if="isModalVisible" @close="hideModal" />

    </div>
</template>

<script>
import ArrowBack from '../components/ArrowBack.vue'
import SaveButton from '../components/SaveButton.vue'
import ExerciseCard from '../components/ExerciseCard.vue'
import AddButton from '../components/AddButton.vue'
import AddExercise from '../components/AddExercise.vue'

export default {
  name: 'MakeTraining',  // переименовано в многословное имя
    components: {
        ArrowBack,
        SaveButton,
        ExerciseCard,
        AddButton,
        AddExercise
    },

    data() {
        return {
            isModalVisible: false
        };
    },

    methods: {
        showModal() {
            console.log('Modal should appear');
            this.isModalVisible = true;
        },

        hideModal() {
            console.log('Modal hidden'); 
            this.isModalVisible = false;
        }
    }
};
</script>

<style scoped>
.header_training_page {
    margin: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header_training_page h1 {
    font-size: 110px;
    color: #fff;
    margin: 0px;
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

.ExerciseCards_Container {
    margin: 0px 10px 10px 10px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 20px;
}


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
    overflow-y: auto;
}

.ExerciseCard {
    margin-bottom: 20px;
}

</style>
