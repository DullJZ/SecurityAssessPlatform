<template>
  <div>
    <el-menu router :default-active="getActiveIndex">
      <el-menu-item index="/exp">
        首页
      </el-menu-item>
      <el-menu-item index="/exp/my-exp">我的实验</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "ExpMenu",
  computed: {
    getActiveIndex(){
      return this.$route.path
    }
  }
}
</script>

<style scoped>

</style>