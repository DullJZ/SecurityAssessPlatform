const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    config
    .plugin('html')
    .tap(args => {
      args[0].title = "网络安全能力评估平台"
      return args
    })
  }
})
