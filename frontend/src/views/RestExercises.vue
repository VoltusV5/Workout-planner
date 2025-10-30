
<template>
    <div class="doing_user_exercises">
        <div class="header">
            <ProgressBar />
            <div class="left">
                <ArrowBack />
            </div>
        </div>
        
        <div class="info">
            <h2>Осталось</h2>
            <h1>00:30</h1>
        </div>

        <div class="buttons">
            <button class="Increase_rest">+20s</button>
            <button class="Skip_rest">Пропустить</button>
        </div>
    </div>
</template>

<script>
import ProgressBar from '../components/ProgressBar.vue'
import ArrowBack from '../components/ArrowBack.vue'

export default {
    name: 'DoingExercises', 
    components: {
        ProgressBar,
        ArrowBack,
    },
        
};
</script>

<style scoped>


.left {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 16px;
    padding-left: 70px;
}



.info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.info h2 {
    font-size: 100px;
    color: #fff;
    margin: 20px;
}

.info h1 {
    font-size: 130px;
    color: #fff;
    margin: 0px;
}


.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 250px;
}

.Increase_rest {
    background-color: #8C8C8C;
    color: #fff;
    width: 400px;
    height: 150px;
    border-radius: 48px;
    font-size: 60px;
}

.Skip_rest {
    background-color: #7C4DFF;
    color: #fff;
    width: 400px;
    height: 150px;
    border-radius: 48px;
    font-size: 60px;
}

</style>
