<template>
<div>
  <h1>xhcms</h1>
  <el-tabs v-model="activeTabName" lazy type="border-card">
    <el-tab-pane name="trafficMonitor" label="流量监控">
      <div>
        <el-row :gutter="24">
          <el-col :span="8">
            <el-statistic
                group-separator=","
                :value="packetData.stats.normal"
                title="今日总请求"
            ></el-statistic>
          </el-col>
          <el-col :span="8">
            <el-statistic
                group-separator=","
                :value="packetData.stats.suspicious"
                title="可疑请求"
            ></el-statistic>
          </el-col>
          <el-col :span="8">
            <el-statistic
                group-separator=","
                :value="packetData.stats.malicious"
                title="恶意请求"
            ></el-statistic>
          </el-col>
        </el-row>
      </div>
      <div style="margin: 20px">图表分析区</div>
      <div>
        <el-button type="primary" @click="queryPackets" style="margin: 10px">刷新数据</el-button>
        <el-table :data="packetData.data" height="500px" border stripe>
          <template slot="empty">
            <el-empty></el-empty>
          </template>
          <el-table-column type="expand">
            <template slot-scope="scope">
              <el-descriptions :column="1" style="padding-left: 20px" label-class-name="packet-detail-label" content-class-name="packet-detail-content">
                <el-descriptions-item v-for="(value,key) in scope.row.httpHeader" :key="key" :label="key===''?'first-line':key">{{value}}</el-descriptions-item>
              </el-descriptions>
            </template>
          </el-table-column>
          <el-table-column type="index"></el-table-column>
          <el-table-column label="状态" width="75px">
            <template>
              <el-tag type="primary">正常</el-tag>
            </template>
          </el-table-column>
<!--          <el-table-column label="ID" prop="id"></el-table-column>-->
          <el-table-column label="请求时间" prop="timestamp"></el-table-column>
          <el-table-column label="顶层协议" prop="topLayer"></el-table-column>
          <el-table-column label="源IP" prop="srcIp"></el-table-column>
          <el-table-column label="目的IP" prop="dstIp"></el-table-column>
          <el-table-column label="请求资源">
            <template slot-scope="scope">{{scope.row.httpHeader['']}}</template>
          </el-table-column>
          <el-table-column label="内容MIME" prop="httpHeader.content_type"></el-table-column>
          <el-table-column label="状态码">
            <template slot-scope="scope">
              <el-tag v-if="scope.row.httpHeader.response_code" :type="scope.row.httpHeader.response_code==='200'?'success':'warning'">{{scope.row.httpHeader.response_code}}</el-tag>
            </template>
          </el-table-column>

        </el-table>
      </div>



    </el-tab-pane>
    <el-tab-pane name="other" label="更多功能">
      <h1>正在开发中</h1>
    </el-tab-pane>
  </el-tabs>
</div>
</template>

<script>
export default {
  name: "PacketView.vue",

  data(){
    return{
      activeTabName: "trafficMonitor",
      packetData:{
        stats:{
          normal: 0,
          suspicious: 0,
          malicious: 0
        },
        data:[
          // {
          //   id:null,
          //   timestamp:null,
          //   topLayer:null,
          //   srcIp:null,
          //   dstIp:null,
          //   uri:null,
          //   responseCode:null,
          //   contentType:null,
          //   httpHeader:{
          //     '': 's',
          //     'date': '2023',
          //     'server': 'apache'
          //   }
          // }
        ]
      }
    }
  },
  methods: {
    queryPackets(){
      this.$axios.get("/packet/xhcms/queryLatest",{
        params:{
          nums: 10
        }
      }).then((res) =>{
        this.packetData.data = res.data.data
      }).catch((err) =>{
        console.log(err)
        this.$message.error(err)
      })
    }
  },
  mounted() {
    this.queryPackets()
  }
}
</script>

<style>
.packet-detail-label{
  font-weight: bold;
  font-style: italic;
}
.packet-detail-content{

}
</style>