
<template>
    <div class="Your_Training">
        <p>Тренировка №1</p>
        <draggable 
            v-show="true" 
            :list="trainingExercises"
            group="exercises" 
            @start="$emit('start-drag')"
            @end="$emit('end-drag')"
            class="Your_Training-ExerciseCards_Container"
            @update:list="updateYourTraining"
        >
            <template v-if="trainingExercises.length === 0" #header >
                <h1 class="Container_empty_alertInfo_ExerciseCards_Container">
                    Перетащите сюда упражнения
                </h1>
            </template>                    
            <template v-slot:item="{ element }">
                <ExerciseCard :key="element.id" :exercise="element" />
            </template>
        </draggable>
    </div>
</template>


<script>

import ExerciseCard from '../components/ExerciseCard.vue'
import draggable from 'vuedraggable';

export default {
  name: 'YourTraining', // Название компонента
    components: {
        ExerciseCard,
        draggable
    },


    props: {
        YourTraining: {
                type: Array,
                required: true,
            },
            showModal: {
                type: Function,
                required: true,
            },
            drag: {
                type: Boolean,
                required: true,
            },
        },
    methods: {
        startDrag() {
            this.$emit('update:drag', true);
        },

        endDrag() {
            this.$emit('update:drag', false);
        },


        updateYourTraining(newYourTraining) {
            this.$emit('update:YourTraining', newYourTraining)
            },
        }
    };

</script>

<style scoped>
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
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    overflow-y: auto;
    width: 100%;
    min-width: 120px;
    min-height: 720px;
}


.Container_empty_alertInfo_ExerciseCards_Container {
    color: red;
    padding: 20px;
    font-size: 24px;
    border: 1px solid #ccc;
    border-bottom: 600px solid transparent;
}



.ExerciseCard {
    margin-bottom: 20px;
}
</style>
