

<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-color: #2D2D2D;;
}

body {
  background: #2D2D2D;
  margin: 0;
  padding: 0;
}

@media screen and (min-width: 1920px) {
    body {
        font-size: 18px; /* Увеличиваем размер шрифта */
    }

    .container {
        width: 90%; /* Устанавливаем ширину контейнера, чтобы он не выходил за экран */
        margin: 0 auto;
    }

    .button {
        width: 200px;
        height: 60px;
        font-size: 20px;
    }
}


</style>
