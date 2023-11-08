<template>
  <div class="main-layout">
    <el-container class="header-container">
      <el-header>
        <h1>网络安全能力评估平台</h1>
      </el-header>
    </el-container>
    <el-container class="body-container">
      <el-aside>
        <slot name="aside"></slot>
      </el-aside>
      <el-main>
        <slot name="main"></slot>
      </el-main>
    </el-container>
    <el-container class="footer-container">
      <el-footer>
        footer
      </el-footer>
    </el-container>
  </div>

</template>

<script>
export default {
  name: "MainLayout"
}
</script>

<style scoped>
.header-container{
  background: #2b4b6b;
  color: white;
  position: sticky;
  top: 0;
  z-index: 100;
  height: 60px;
}
.body-container{
  height: 80%;
}
.footer-container{
  border-top: black 1px solid;
  z-index: 100;
  bottom: 0;
  height: 10%;
}
.main-layout{
  height: 100vh;
}
</style>