
<template>
    <div class="choose_page">
        <div class="header_choose_page">
            <ArrowBack action="goHome" />
            <h1>Выбор тренировки</h1>
        </div>
        <div class="user_trainings_container">
            <div class="user_trainings">
                <router-link to='/doing_exercises' class="no-underline">
                    <YourTraining class="YourTraining"
                    :YourTraining="trainingExercises" 
                    @update:YourTraining="updateYourTraining"
                    @update:drag="updateDrag"
                    :showModal="showModal" 
                    :drag="drag" 
                    />
                </router-link>
                <router-link to='/edit_training' class="no-underline">
                    <EditButton />
                </router-link>
            </div>
            <div class="user_trainings">
                <router-link to='/doing_exercises' class="no-underline">
                    <YourTraining class="YourTraining"
                    :YourTraining="trainingExercises" 
                    @update:YourTraining="updateYourTraining"
                    @update:drag="updateDrag"
                    :showModal="showModal" 
                    :drag="drag" 
                    />
                </router-link>
                <router-link to='/edit_training' class="no-underline">
                    <EditButton />
                </router-link>
            </div>
            <div class="user_trainings">
                <router-link to='/doing_exercises' class="no-underline">
                    <YourTraining class="YourTraining"
                    :YourTraining="trainingExercises" 
                    @update:YourTraining="updateYourTraining"
                    @update:drag="updateDrag"
                    :showModal="showModal" 
                    :drag="drag" 
                    />
                </router-link>
                <router-link to='/edit_training' class="no-underline">
                    <EditButton />
                </router-link>
            </div>
            <div class="user_trainings">
                <router-link to='/doing_exercises' class="no-underline">
                    <YourTraining class="YourTraining"
                    :YourTraining="trainingExercises" 
                    @update:YourTraining="updateYourTraining"
                    @update:drag="updateDrag"
                    :showModal="showModal" 
                    :drag="drag" 
                    />
                </router-link>
                <router-link to='/edit_training' class="no-underline">
                    <EditButton />
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import { trainingExercises } from '@/assets/data/trainingExercises'

import ArrowBack from '../components/ArrowBack.vue'
import YourTraining from '../components/YourTraining.vue'
import EditButton from '../components/EditButton.vue'

export default {
    name: 'ChooseTraining',
    components: {
        ArrowBack,
        YourTraining,
        EditButton,
    },


    data() {
        return {
            trainingExercises: Array.isArray(trainingExercises) ? trainingExercises : [],
            drag: false,
        };
    
    },
    methods: {

        updateYourTraining(newYourTraining) {
        this.trainingExercises = Array.isArray(newYourTraining) ? newYourTraining : [];
        },
        updateDrag(newDragStatus) {
        this.drag = newDragStatus;
        },
        showModal() {
            console.log('Modal should appear');
        }
    },
};

</script>

<style scoped>

.user_trainings_container {
    display: flex;
    justify-content: center;
    overflow-y: auto;
    
}

.YourTraining {
    height: 800px;
}

.header_choose_page {
    margin: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.header_choose_page h1  {
    font-size: 120px;
    color: #fff;
    text-align: center;
    margin: 0px;
    flex-grow: 1;
}

.no-underline {
    text-decoration: none;
}



</style>
