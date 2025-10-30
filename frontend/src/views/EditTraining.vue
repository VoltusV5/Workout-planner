
<template>
    <div class="make_training_page">
        <div class="header_training_page">
            <ArrowBack action="goChooseTraining" />
            <h1>Редактирование тренировки</h1>
            <SaveButton />
        </div>
        
        <CatalogExercises 
            :catalogExercises="catalogExercises" 
            @update:catalogExercises="updateCatalogExercises"
            @update:drag="updateDrag"
            :showModal="showModal" 
            :drag="drag" 
        />



        <YourTraining 
            :YourTraining="trainingExercises" 
            @update:YourTraining="updateYourTraining"
            @update:drag="updateDrag"
            :showModal="showModal" 
            :drag="drag" 
        />


        <AddExercise 
            v-if="isModalVisible" 
            @close="hideModal" 
        />

    </div>
</template>

<script>

import { trainingExercises } from '@/assets/data/trainingExercises'
import { catalogExercises } from '@/assets/data/catalogExercises'


import ArrowBack from '../components/ArrowBack.vue'
import SaveButton from '../components/SaveButton.vue'
import AddExercise from '../components/AddExercise.vue'
import CatalogExercises from '../components/CatalogExercises.vue'
import YourTraining from '../components/YourTraining.vue'

export default {
    name: 'MakeTraining', 
    components: {
        ArrowBack,
        SaveButton,
        AddExercise,
        CatalogExercises,
        YourTraining
    },

    
    data() {
        return {
            trainingExercises: Array.isArray(trainingExercises) ? trainingExercises : [],
            catalogExercises: Array.isArray(catalogExercises) ? catalogExercises : [],
            isModalVisible: false,
            
            drag: false,
        };
    
    },
    methods: {

        updateDrag(newDragStatus) {
            this.drag = newDragStatus;
        },

        updateCatalogExercises(newCatalogExercises) {
            this.catalogExercises = newCatalogExercises;
        },

        updateYourTraining(newYourTraining) {
            this.trainingExercises = newYourTraining;
        },

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
    font-size: 90px;
    color: #fff;
    margin: 0px;
}

.no-underline {
    text-decoration: none;
}

</style>
