
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
                <draggable v-if="catalogExercises && catalogExercises.length > 0" v-model="catalogExercises" group="exercises" @start="drag=true" @end="drag=false">
                    <template v-slot:default="{ element }">
                        <ExerciseCard :key="element.id" :exercise="element" />
                    </template>
                </draggable>
                
            </div>
        </div>
        <div class="Your_Training">
            <p>Тренировка №1</p>
            <div class="Your_Training-ExerciseCards_Container">
                <draggable v-if="trainingExercises && trainingExercises.length > 0" v-model="trainingExercises" group="exercises" @start="drag=true" @end="drag=false">
                    <template v-slot:default="{ element }">
                        <ExerciseCard :key="element.id" :exercise="element" />
                    </template>
                </draggable>
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
import draggable from 'vuedraggable';

export default {
  name: 'MakeTraining',  // переименовано в многословное имя
    components: {
        ArrowBack,
        SaveButton,
        ExerciseCard,
        AddButton,
        AddExercise,
        draggable
    },

    data() {
        return {
            isModalVisible: false,
            catalogExercises: [
                { 
                    id: 1, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 2, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 3, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 4, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 5, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 6, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 7, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                },
                { 
                    id: 8, 
                    name: 'Push Up', 
                    time: 40, 
                    reps: 15, 
                    image: '../assets/make_training/image_card.png'
                }
            ],
            trainingExercises: [
            ],
            drag: false,
        };
    },
    mounted() {
        // Проверьте, что данные существуют в момент рендера
        console.log('Mounted method is called');
        console.log('Catalog Exercises:', this.catalogExercises);
        console.log('Training Exercises:', this.trainingExercises);
        this.catalogExercises.forEach(exercise => {
            console.log(exercise);
        });
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
