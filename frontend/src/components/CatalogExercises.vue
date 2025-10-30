
<template>
    <div class="CatalogExercises">
        <div class="CatalogExercises_header">
            <p>Каталог упражнений</p>
            <AddButton @click="showModal" />
        </div>
        
        <draggable 
            v-show="true" 
            :list="catalogExercises"
            group="exercises" 
            @start="$emit('start-drag')"
            @end="$emit('end-drag')"
            class="ExerciseCards_Container"
            @update:list="updateCatalogExercises"
        >
            <template v-if="catalogExercises.length === 0" #header >
                <h1 class="Container_empty_alertInfo_catalogExercises">
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
import AddButton from '../components/AddButton.vue'
import ExerciseCard from '../components/ExerciseCard.vue'
import draggable from 'vuedraggable';

export default {
  name: 'CatalogExercises',
    components: {
        AddButton,
        ExerciseCard,
        draggable
    },
    props: {
        catalogExercises: {
                type: Array,
                required: true,
                default: () => [],
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


        updateCatalogExercises(newCatalogExercises) {
            this.$emit('update:catalogExercises', newCatalogExercises)
            },
        }
    };
</script>

<style scoped>

.ExerciseCards_Container {
    margin: 0px 10px 10px 10px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 20px;
    overflow-y: auto;
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



.Container_empty_alertInfo_catalogExercises {
    color: red;
    padding: 20px;
    font-size: 24px;
    border: 1px solid #ccc;
    border-bottom: 500px solid transparent;
    border-right: 1000px solid transparent;
}

.ExerciseCard {
    margin-bottom: 20px;
}
</style>
