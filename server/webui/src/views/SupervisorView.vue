<template>
  <div>
    <main-layout>
      <template slot="aside">
        <sup-menu></sup-menu>
      </template>
      <template slot="main">
        <router-view></router-view>
      </template>
    </main-layout>
  </div>
</template>

<script>
import MainLayout from "@/components/MainLayout";
import SupMenu from "@/components/SupMenu";
export default {
  components: {SupMenu, MainLayout}
}
</script>

<style>

</style>