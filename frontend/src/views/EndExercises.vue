<template>
    <div>
        <h1 class="main_page_header">Тренировка окончена</h1>

        <main class="main_page_container">
            <div class="photo_div-sport_man">
                <img src="../assets/main_page/sport_man.png">
            </div>
            
            <div class="main_div-buttons">
                <img src="../assets/main_page/image 2.png" />
                <!-- Кнопка для создания тренировки -->
                <router-link to="/" class="no-underline">
                    <button class="goHome">На главную</button>
                </router-link>
            </div>
            <div class="photo_div-sport_woman">
                <img src="../assets/main_page/sport_woman.png">
            </div>
        </main>
    </div>
</template>

<script>
export default {
    name: 'EndExercises',
};

</script>

<style scoped>

.main_page_header {
    font-size: 120px;
    color: #fff;
    text-align: center;
    margin: 10px;
}

.main_div-buttons {
    text-decoration: none;
}

.no-underline {
    text-decoration: none;
}

.goHome {
    width: 800px;
    height: 200px;
    border-radius: 48px;
    background-color: #7C4DFF;

    color: #fff;
    font-size: 60px;
    margin: 20px auto;
}

.photo_div-sport_woman {
    height: 894px;

}

.photo_div-sport_man {
    height: 917px;
}

.main_page_container {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>
