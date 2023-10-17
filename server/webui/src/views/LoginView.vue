<template>
  <div class="login-view">
    <div class="login-container">
      <div class="login-title">
        <h1>网络安全能力评估系统</h1>
      </div>
      <div class="login-form">
        <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-width="0px" class="login-form-container" action="/exp">
          <el-form-item prop="username">
            <el-input v-model="loginForm.username" placeholder="用户名" prefix-icon="el-icon-user" clearable
                      @keyup.enter.native="handleLogin"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="loginForm.password" placeholder="密码" prefix-icon="el-icon-lock" show-password
                      @keyup.enter.native="handleLogin"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handleLogin">登录</el-button>
            <el-button @click="register">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginForm: {
        username: "",
        password: ""
      },
      loginRules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.$refs.loginForm.submit()
        }
      })
    },
    register(){
      this.$message.error('注册功能暂未开放')
    },
  }
}
</script>

<style scoped>
.login-view {
  width: 100%;
  height: 100%;
  background-color: #2b4b6b;
}

.login-container {
  width: 350px;
  /*background-color: #fff;*/
  border-radius: 5px;
  position: absolute;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -50%);
}

.login-title {
  width: 100%;
  height: 50px;
  line-height: 50px;
  border-bottom: 1px solid #ddd;
  color: white;
}

.login-form {
  width: 100%;
  margin-top: 20px;
  /* border: 1px solid #ddd; */
  /* border-radius: 5px; */
  /* padding: 20px; */
}

.login-form-container {
  width: 100%;
  height: 100%;
}
</style>