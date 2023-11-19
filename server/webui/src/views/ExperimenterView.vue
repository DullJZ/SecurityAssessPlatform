<template>
  <div>
    Login As A Experimenter ...
    <main-layout>
      <template slot="aside">
        <exp-menu></exp-menu>
      </template>
      <template slot="main">
        <router-view></router-view>
      </template>
    </main-layout>
  </div>
</template>

<script>
import MainLayout from "@/components/MainLayout";
import ExpMenu from "@/components/ExpMenu";
export default {
  components: {ExpMenu, MainLayout}
}
</script>

<style>

</style>