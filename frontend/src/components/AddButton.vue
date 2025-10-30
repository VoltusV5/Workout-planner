
<template>
    <div class="AddButton">
        <button @click="handleClick">+</button>
    </div>
</template>


<script>
export default {
    name: 'AddButton',

    methods: {
        handleClick() {
            this.$emit('click');
        }
    }
};
</script>

<style scoped>

button {
    background-color: #7C4DFF;
    color: #fff;
    width: 100px;
    height: 100px;
    border-radius: 24px;
    font-size: 60px;
}

</style>
