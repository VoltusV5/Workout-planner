
<template>
    <div class="ExerciseCard">
            <h3>{{ exercise.name }}</h3>
            <img class="ExerciseCard_image" :src="exercise.image" alt="Exercise Image">
            <h5>{{ exercise.time }} сек</h5>
            <h6>x{{ exercise.reps }} на каждую сторону</h6>
    </div>
</template>


<script>
export default {
    name: 'ExerciseCard', 

    props: {
        exercise: {
            type: Object,
            required: true,
        }
    },

    data() {
        return {
        };
    },

    methods: {
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
