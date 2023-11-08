<template>
<div>
  <h1>{{ test }}</h1>
</div>
</template>

<script>
export default {
  name: "ExpHistoryView",
  data(){
    return{
      test: ''
    }
  },
  mounted() {
    // 5s后将this.test赋值
    setTimeout(() => {
      this.test = 'test'
    }, 5000)
  }
}
</script>

<style scoped>

</style>