<template>
    <div>
        <h1 class="main_page_header">Workout Planner</h1>

        <main class="main_page_container">
            <div class="photo_div-sport_man">
                <img src="../assets/main_page/sport_man.png">
            </div>
            <div class="main_div-buttons">
                <!-- Кнопка для начала тренировки -->
                <button class="go_training">Заниматься</button>

                <!-- Статистика -->
                <div class="stats-container">
                    <p class="stat-item">💪 Проведено тренировок:</p>
                    <p class="stat-item number">{{ workoutsCount }}🔥</p>
                    <p class="stat-item"></p>
                </div>
                <!-- Кнопка для создания тренировки -->
                <button class="make_training">Составить тренировку</button>
            </div>
            <div class="photo_div-sport_woman">
                <img src="../assets/main_page/sport_woman.png">
            </div>
        </main>
    </div>
</template>

<script>
export default {
  name: 'HomePage', // Название компонента
    data() {
    return {
      workoutsCount: 159, // Значение для отображения, можно связать с backend
    };
    },
};

</script>

<style scoped>

.main_page_header {
    font-size: 120px;
    color: #fff;
    text-align: center;
}

.go_training {
    width: 500px;
    height: 500px;
    border-radius: 48px;
    background-color: #7C4DFF;

    color: #fff;
    font-size: 70px;
    
    margin: 20px auto;
    display: block;
}

.stats-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px auto;
}

.stat-item {
    font-size: 40px;
    color: #fff;
    margin: 0 10px;
}

.number {
    color: orange;
}

.make_training {
    width: 1000px;
    height: 200px;
    border-radius: 48px;
    background-color: #404040;

    color: #fff;
    font-size: 60px;
    margin: 20px auto;
    display: block;
}

.photo_div-sport_woman {
    width: 1340px;
    height: 894px;

}

.photo_div-sport_man {
    width: 1631px;
    height: 917px;
}

.main_page_container {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>
