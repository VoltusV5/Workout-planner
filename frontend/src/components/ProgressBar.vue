
<template>
    <div class="progressBar">
        <div class="exercise done"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
        <div class="exercise"></div>
    </div>
</template>

<script>
export default {
    name: 'ProgressBar',
};
</script>

<style scoped>

.progressBar {
    display: flex;
    justify-content: center;
    margin: 10px;
}

.exercise {
    background-color: #D9D9D9;
    width: 100px;
    height: 30px;
    margin: 10px;
    border-radius: 15px;
    text-align: center;
}

.done{
    background-color: #7C4DFF;
}

</style>
