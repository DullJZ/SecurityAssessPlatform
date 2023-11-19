<template>
  <div>
    <el-tabs>
      <el-tab-pane label="实时监控" lazy>
        <exp-watch-view></exp-watch-view>
      </el-tab-pane>
      <el-tab-pane label="发布实验" lazy>
        <exp-publish-view></exp-publish-view>
      </el-tab-pane>
      <el-tab-pane label="实验记录" lazy>
        <exp-history-view></exp-history-view>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import ExpPublishView from "@/components/ExpPublishView";
import ExpWatchView from "@/components/ExpWatchView";
import ExpHistoryView from "@/components/ExpHistoryView";
export default {
  name: "ExpView",
  components: {ExpHistoryView, ExpWatchView, ExpPublishView}
}
</script>

<style scoped>

</style>