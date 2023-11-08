<template>
  <div>
    <el-menu router :default-active="getActiveIndex">
      <el-menu-item index="/sup">
        首页
      </el-menu-item>
      <el-menu-item index="/sup/class">班级管理</el-menu-item>
      <el-menu-item index="/sup/exp">
        实验管理
      </el-menu-item>
      <el-menu-item index="/sup/images">镜像管理</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "SupMenu",
  computed: {
    getActiveIndex(){
      return this.$route.path
    }
  }
}
</script>

<style scoped>

</style>