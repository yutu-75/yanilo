<template>
	<div class="box">
		<img src="../../static/img/Loginbg.3377d0c.jpg" alt="">
		<div class="register">
      <div class="login-title">
				<img src="../../static/img/Logotitle.1ba5466.png" alt="">
				<p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p>
			</div>
			<div class="register_box">
        <div class="register-title">注册路飞学城</div>
				<div class="inp">
					<input v-model = "mobile" type="text" placeholder="手机号码" class="user" @blur="checkPhone">
					<input v-model = "password" type="password" placeholder="密码" class="user">
					<input v-model = "r_password" type="password" placeholder="确认密码" class="user">

					<div>
            <input v-model = "sms" type="text" placeholder="输入验证码" class="user" style="width: 62%">
            <button style="width: 34%;height: 41px;" @click="getSmsCode" :disabled="this.flag">{{btn_msg}}</button>
          </div>
					<button class="register_btn" @click="registerHandler">注册</button>
					<p class="go_login" >已有账号 <router-link to="/user/login">直接登录</router-link></p>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
  name: 'Register',
  data(){
    return {
        sms:"",
        mobile:"",
        password:"",
        r_password:"",
        validateResult:false,
        interval_time:60,  // 倒计时时间
        btn_msg:'点击获取验证码',
        flag:false,  // 判断定时器 是否已经开启
        // disabled:true,

    }
  },
  created(){
  },
  methods:{
    checkPhone(){

      let phoneNumber = this.mobile;
      // 前端
      let reg = /^1[3-9][0-9]{9}$/;
      if (!reg.test(phoneNumber)){
        this.$message.error('手机号 格式 error');
        return false;
      }
      // 发送请求
      this.$axios.get(`${this.$settings.Host}/users/check_phone/?phone=${phoneNumber}`)  // request.GET.get(phone)
      .then((res)=>{
        console.log(res);
      }).catch((error)=>{
        this.$message.error(error.response.data.error_msg);
      })

    },

    registerHandler(){

      this.$axios.post(`${this.$settings.Host}/users/register/`,{
        sms:this.sms,
        phone:this.mobile,
        password:this.password,
        r_password:this.r_password,
      }).then((res)=>{
        sessionStorage.token = res.data.token;
        sessionStorage.username = res.data.username;
        sessionStorage.id = res.data.id;
        this.$router.push('/');

      }).catch((error)=>{
        console.log(error.response);
      })
    },

    // 点击获取验证码
    getSmsCode(){
      this.$axios.get(`${this.$settings.Host}/users/sms_code/${this.mobile}/`)
      .then((res)=>{
        if (!this.flag){
          this.flag = setInterval(()=>{
            if (this.interval_time > 0){
              this.interval_time--;
              this.btn_msg = `${this.interval_time}秒后重新获取`;

            }else {
              this.interval_time=60;
              this.btn_msg = '点击发送验证码'
              clearInterval(this.flag);
              this.flag = false;
            }
          },1000)
        }


      })
      .catch((error)=>{
        this.$message.error(error.response.data.msg);
      })


    }


  },

};
</script>

<style scoped>
.box{
	width: 100%;
  height: 100%;
	position: relative;
  overflow: hidden;
}
.box img{
	width: 100%;
  min-height: 100%;
}
.box .register {
	position: absolute;
	width: 500px;
	height: 400px;
	top: 0;
	left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}
.register .register-title{
    width: 100%;
    font-size: 24px;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #4a4a4a;
    letter-spacing: .39px;
}
.register-title img{
    width: 190px;
    height: auto;
}
.register-title p{
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
}
.login-title{
    margin-top:100px;
    width: 100%;
    text-align: center;
}
.login-title img{
    width: 190px;
    height: auto;
}
.login-title p{
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
}
.register_box{
    width: 400px;
    height: auto;
    background: #fff;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
}
.register_box .title{
	font-size: 20px;
	color: #9b9b9b;
	letter-spacing: .32px;
	border-bottom: 1px solid #e6e6e6;
	 display: flex;
    	justify-content: space-around;
    	padding: 50px 60px 0 60px;
    	margin-bottom: 20px;
    	cursor: pointer;
}
.register_box .title span:nth-of-type(1){
	color: #4a4a4a;
    	border-bottom: 2px solid #84cc39;
}

.inp{
	width: 350px;
	margin: 0 auto;
}
.inp input{
    border: 0;
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}
.inp input.user{
    margin-bottom: 16px;
}
.inp .rember{
     display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
}
.inp .rember p:first-of-type{
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
}
.inp .rember p:nth-of-type(2){
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
}

.inp .rember input{
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}

.inp .rember p span{
    display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
/*left: 20px;*/

}
#geetest{
	margin-top: 20px;
}
.register_btn{
     width: 100%;
    height: 45px;
    background: #84cc39;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
}
.inp .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
}
.inp .go_login span{
    color: #84cc39;
    cursor: pointer;
}
</style>
