
<template>
    <div class="doing_user_exercises">
        <div class="header">
            <ProgressBar />
            <div class="left">
                <ArrowBack />
            </div>
        </div>
        
        <div class="exercise">
            <div class="video_container">
                <img src="../assets/make_training/image_card.png" class="video" />
            </div>
            <div class="exercise_info">
                <h1>x 30</h1>
                <h3>Классический пресс</h3>
                <h5>x15 на каждую сторону</h5>

            </div>
        </div>

        <div class="buttons">
            <ArrowBack />
            <NextButton />
            <ArrowBack class="mirrored" />
        </div>
    </div>
</template>

<script>
import ProgressBar from '../components/ProgressBar.vue'
import ArrowBack from '../components/ArrowBack.vue'
import NextButton from '@/components/NextButton.vue';

export default {
  name: 'DoingExercises', 
    components: {
        ProgressBar,
        ArrowBack,
        NextButton,
    },
        
};
</script>

<style scoped>
.doing_user_exercises {
    display: flex;
    flex-direction: column;
}

.left {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 16px;
    padding-left: 70px;
}

.video {
    width: 955px;
}

.exercise {
    display: flex;
    justify-content: right;
    align-items: center;
}

.exercise_info {
    padding: 50px;
}

.exercise_info h1 {
    font-size: 100px;
    color: #fff;
}

.exercise_info h3 {
    font-size: 60px;
    color: #fff;
    margin: 20px;
}

.exercise_info h5 {
    font-size: 40px;
    color: #fff;
    opacity: 70%;
    margin: 0px;
}

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 50px;
}

.mirrored {
    transform: scaleX(-1);  
}

</style>
