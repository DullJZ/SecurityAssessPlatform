<template>
  <div>
    <el-container>
      <el-header>
        <h1>熊海内容管理系统监控</h1>
      </el-header>
      <el-main>
        <el-row :gutter="20">
          <el-col :span="6">
            <el-card shadow="hover">
              <el-row>
                <el-table :data="ipTable">
                  <el-table-column prop="time" label="访问时间"></el-table-column>
                  <el-table-column prop="ip" label="IP地址"></el-table-column>
                </el-table>
              </el-row>
            </el-card>
          </el-col>
          <el-col :span="18">
            <el-card shadow="hover">
              IP2
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>

</template>

<script>
export default {
  name: "MonitorView",
  data(){
    return{
      ipTable:[
        {
          time: 0,
          ip :1,
        },
        {
          time: 0,
          ip :1,
        },
      ]
    }
  }
}
</script>

<style scoped>

</style>