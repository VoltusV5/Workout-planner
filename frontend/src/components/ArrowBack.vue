
<template>
    <div class="Arrow_Back">
    <!-- Основная разметка компонента -->
        <button class="Arrow_Back_btn" @click="handleClick">
            <img src="../assets/make_training/Arrow.png">
        </button>
    </div>
</template>


<script>
export default {
  name: 'ArrowBack', // Название компонента

    props: {
        action: {
            type: String,
            default: 'closeModal'
        }
    },

    data() {
    return {
      // Локальное состояние компонента
    };
    },

    methods: {
        handleClick() {
            if (this.action === 'goHome') {
                this.$router.push('/');
            } else {
                this.$emit('close');
            }
        }
    },
};
</script>

<style scoped>


.Arrow_Back button {
    color: #fff;
    opacity: 20%;
    border-radius: 24px;
    width: 100px;
    height: 100px;
}

.Arrow_Back_btn img{
    opacity: 100%;
}

    
</style>
