
<template>
  <div class="SaveButton">
        <button><img src="../assets/make_training/Arrow.png" class="mirrored" /></button>
  </div>
</template>


<script>
export default {
  name: 'SaveButton',

  props: {
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

button {
    background-color: #7C4DFF;
    color: #fff;
    width: 300px;
    height: 100px;
    border-radius: 48px;
    font-size: 60px;
}

.mirrored {
  transform: scaleX(-1);
}

</style>
